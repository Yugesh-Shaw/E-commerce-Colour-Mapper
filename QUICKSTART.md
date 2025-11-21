# Quick Start Guide - AI Color Mapper

*Get running in 15 minutes - Created by Yugesh*

## 🎯 What This Does

Maps multilingual product colors (French, German, Italian, etc.) to standardized codes using OpenAI CLIP vision model.

**Example**: "bleu marine" (French) → `NAVY_BLUE`

---

## 📋 Prerequisites

- [ ] Python 3.8+ installed
- [ ] Google Colab account (free tier works)
- [ ] Excel file with color data
- [ ] Product image URLs (optional but recommended)

---

## 🚀 Step-by-Step Setup

### Step 1: Setup Environment (5 min)

**On Google Colab:**

```python
# Cell 1: Install dependencies
!pip install torch transformers pillow aiohttp nest-asyncio pandas openpyxl -q

# Cell 2: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
```

### Step 2: Prepare Excel File (5 min)

Create Excel with **TWO sheets**:

**Sheet 1: "Postman - Colour Code"** (Your allowed colors)
```
values.value.label  | values.value.code
--------------------|------------------
Navy Blue           | NAVY_BLUE
Forest Green        | FOREST_GREEN
Crimson Red         | CRIMSON_RED
Olive Green         | OLIVE_GREEN
```

**Sheet 2: "Colour Mapping"** (Products to map)
```
colour                    | Image Link
--------------------------|----------------------------------
marine foncé / 24         | https://example.com/product1.jpg
vert olive                | https://example.com/product2.jpg
rouge bordeaux / XL       | https://example.com/product3.jpg
```

Upload to: `/content/drive/MyDrive/Color Map/Colour_Map_Template.xlsx`

### Step 3: Run the Script (5 min)

```python
# Cell 3: Update paths and run
FILE_PATH = '/content/drive/MyDrive/Color Map/Colour_Map_Template.xlsx'
OUTPUT_FILE = '/content/drive/MyDrive/Color Map/Output.xlsx'

# Run the color mapper
!python color_mapper.py
```

---

## 📊 Understanding Results

**Output Excel will have:**

| colour | Image Link | Mapped Colour Code | CLIP Suggestions | CLIP Confidence |
|--------|------------|-------------------|------------------|-----------------|
| marine foncé | https://... | NAVY_BLUE | Navy Blue | 0.89 |
| vert olive | https://... | OLIVE_GREEN | Olive Green | 0.82 |

**Confidence Guide:**
- **≥ 0.80**: ✅ Auto-accept (high confidence)
- **0.60-0.79**: ⚠️ Quick review recommended
- **< 0.60**: ❌ Manual mapping needed

---

## 🎯 Common Use Cases

### Use Case 1: French Product Import
```
Input: "bleu marine / taille M"
→ Detects: "bleu marine" = French navy
→ Output: NAVY_BLUE (Conf: 0.88)
```

### Use Case 2: German Colors
```
Input: "olivgrün camo"
→ Detects: "olivgrün" = German olive
→ Output: OLIVE_GREEN (Conf: 0.85)
```

### Use Case 3: Image Verification
```
Input: "couleur spéciale" (ambiguous text)
→ Downloads image
→ CLIP analyzes: "This looks navy blue"
→ Output: NAVY_BLUE (Conf: 0.76)
```

---

## ⚙️ Configuration

**In `color_mapper.py`, adjust:**

```python
# Confidence threshold (stricter = more manual reviews)
CONFIDENCE_THRESHOLD = 0.7  # Default is good

# Image processing (higher = better quality, slower)
IMAGE_SIZE = (1000, 1000)  # Try (512, 512) if memory issues

# Performance
keep_top = 64  # Max colors in family subset
```

---

## 📈 Performance Expectations

| Items | With Images | Text Only |
|-------|-------------|-----------|
| 10 | ~30 sec | ~5 sec |
| 100 | ~5 min | ~30 sec |
| 1,000 | ~50 min | ~5 min |

*Using Google Colab T4 GPU*

---

## 🐛 Troubleshooting

### "CUDA out of memory"
```python
# Use smaller images
IMAGE_SIZE = (512, 512)

# Or clear GPU cache
import torch
torch.cuda.empty_cache()
```

### "Many 'No Match' results"
```python
# Lower threshold
CONFIDENCE_THRESHOLD = 0.5

# Or expand allowed colors list
```

### "Images not downloading"
```python
# Check URLs are accessible
# Increase timeout in code:
async with session.get(url, timeout=60) as response:
```

### "Wrong colors detected"
```python
# Check if images show correct color
# Ensure allowed colors list is comprehensive
```

---

## ✅ Quick Test

**Minimal test (5 items):**

1. Create Excel with 5 test colors
2. Run script
3. Check output confidence scores
4. Spot-check 2-3 random mappings

**If 4/5 are correct → Good to go! Scale up.**

---

## 📞 Need Help?

- Check main [README.md](README.md) for detailed docs
- Review [EXCEL_TEMPLATE.md](EXCEL_TEMPLATE.md) for format specs
- See example outputs in `/examples/` folder

---

## 🎉 Next Steps

1. ✅ Test with 10-20 items
2. ✅ Review confidence scores
3. ✅ Process full dataset
4. ✅ Spot-check random samples
5. ✅ Upload to marketplace

**Typical workflow**: 100 items → 5 min → Review 10-15 flagged → Done! ⚡

---

*Built by Yugesh | Questions? Check the documentation or GitHub issues*
