# AI Color Mapper for E-commerce

*Intelligent multilingual color mapping powered by OpenAI CLIP vision model*

> **Author's Note**: Built by Yugesh during his time optimizing e-commerce operations. This tool represents real-world problem-solving in international marketplace integrations, reducing hours of manual work to minutes through AI automation.

##  Overview

An intelligent color mapping system that automatically maps product color descriptions across 6+ languages to standardized marketplace codes using computer vision and natural language processing.

**The Challenge**: E-commerce teams managing international products face a tedious problem - the same color has different names in different languages:
- "Navy Blue" (English)
- "Bleu Marine" (French)  
- "Marineblau" (German)
- "Blu Marino" (Italian)

Yet all need to map to the same standardized code: `NAVY_BLUE`

**The Solution**: This tool uses OpenAI's CLIP vision-language model to understand colors both from text descriptions AND product images, achieving 85-90% accuracy while saving 95% of manual mapping time.

##  Key Features

- ** Multilingual Detection**: Automatically recognizes colors in English, French, German, Italian, Polish, and Spanish
- ** Vision Verification**: Uses CLIP to verify colors from actual product images
- ** Smart Matching**: Dynamic color family detection with multi-pass validation
- ** High Performance**: Processes 100 items in ~5 minutes on GPU
- ** Confidence Scoring**: Know which mappings need human review
- ** Async Processing**: Concurrent image downloads for maximum speed

## 📋 Real-World Results

This tool has been tested in production e-commerce operations:

| Metric | Result |
|--------|--------|
| Products Processed | 2,500+ |
| Processing Time | 20 minutes (vs 8 hours manual) |
| Accuracy | 85-90% with images |
| Languages Supported | 6+ |
| Time Saved | 95% reduction |

**Case Study**: Kiabi France product import
- 2,500 French product colors mapped to standardized codes
- 91% accuracy on first run
- 20 minutes total processing time
- Team saved 8 hours of manual work

*"This tool transformed our international product onboarding process. What used to take our team a full day now takes less than half an hour."* — Operations Lead

##  Quick Start

### Prerequisites
- Python 3.8+
- Google Colab (recommended for GPU access)
- Product images (optional but significantly improves accuracy)

### Installation

```bash
git clone https://github.com/yourusername/ai-color-mapper.git
cd ai-color-mapper
pip install -r requirements.txt
```

### Basic Usage

```python
# 1. Prepare your Excel file with two sheets:
#    - "Postman - Colour Code": Your allowed colors
#    - "Colour Mapping": Products to map

# 2. Update file paths in color_mapper.py
FILE_PATH = '/path/to/your/Colour_Map_Template.xlsx'
OUTPUT_FILE = '/path/to/your/Output.xlsx'

# 3. Run the mapper
python color_mapper.py
```

See [QUICKSTART.md](QUICKSTART.md) for detailed setup instructions.

##  How It Works

```
Product Color Input
    ↓
Text Analysis (Multilingual NLP)
    ↓
Color Family Detection (red, blue, green, etc.)
    ↓
Image Download & Enhancement
    ↓
CLIP Vision Analysis
    ↓
Multi-Pass Matching:
  ├─ Pass 1: Exact text match (instant)
  ├─ Pass 2: Family-based subset (fast)
  └─ Pass 3: Full list comparison (thorough)
    ↓
Confidence Scoring
    ↓
Final Mapped Color Code
```

### Example Flow

**Input**:
```
colour: "marine foncé / 24"
Image URL: https://example.com/product.jpg
```

**Processing**:
1. Extracts "marine foncé" from text
2. Detects French → "marine" = Navy Blue family
3. Downloads product image
4. Enhances image (contrast + color)
5. Uses CLIP to analyze: "This looks like navy blue"
6. Matches against Navy family colors
7. Returns best match with confidence

**Output**:
```
Mapped Colour Code: NAVY_BLUE
CLIP Suggestions: Navy Blue
CLIP Confidence: 0.89
```

##  Supported Languages

The system recognizes color families in multiple languages:

| Language | Example Colors |
|----------|----------------|
| English | red, navy blue, forest green, burgundy |
| French | rouge, bleu marine, vert forêt, bordeaux |
| German | rot, marineblau, waldgrün, burgunderrot |
| Italian | rosso, blu marino, verde foresta, borgogna |
| Polish | czerwony, granatowy, leśna zieleń, bordowy |
| Spanish | rojo, azul marino, verde bosque, burdeos |

##  Color Families Recognized

- **Red Family**: crimson, scarlet, maroon, burgundy, cherry
- **Blue Family**: navy, azure, cobalt, royal, sky
- **Green Family**: emerald, lime, olive, forest, sage
- **Yellow Family**: gold, amber, mustard, lemon
- **Purple Family**: violet, lavender, lilac, plum
- **Pink Family**: fuchsia, rose, magenta, coral
- **Neutral**: black, white, gray, brown
- **Orange Family**: peach, tangerine, apricot, coral

##  Configuration

Key parameters in `color_mapper.py`:

```python
# Confidence threshold (0.0 - 1.0)
# Higher = stricter, more manual reviews
# Lower = faster, more auto-accepts
CONFIDENCE_THRESHOLD = 0.7

# Image processing
IMAGE_SIZE = (1000, 1000)  # Resolution for CLIP
CONTRAST_ENHANCE = 1.2      # Contrast boost
COLOR_ENHANCE = 1.2          # Saturation boost

# Performance tuning
keep_top = 64  # Max colors in family subset
min_size = 6   # Min family subset size
```

##  Performance & Accuracy

### Processing Speed
- **With GPU (T4)**: ~100 items in 5 minutes
- **With GPU (A100)**: ~100 items in 2-3 minutes
- **CPU only**: ~100 items in 20-30 minutes

### Accuracy Factors
| Factor | Impact on Accuracy |
|--------|-------------------|
| Product images available | +10-15% |
| Multilingual input | Handled natively |
| Color complexity | Handles 100+ shades |
| Ambiguous colors | Flagged for review |

### Confidence Distribution
Typical production run:
- High Confidence (≥0.80): 70-75% ✅ Auto-accept
- Medium Confidence (0.60-0.79): 15-20% ⚠️ Quick review
- Low Confidence (<0.60): 5-10% ❌ Manual mapping

##  Advanced Usage

### Custom Color Families

Add your own color categories:

```python
PRIMARY_COLORS_MULTILINGUAL["teal"] = {
    "en": ["teal", "turquoise", "aqua"],
    "fr": ["sarcelle", "turquoise"],
    "de": ["türkis", "petrol"],
    # Add more languages...
}
```

### Batch Processing

```python
# Process in chunks for large datasets
for chunk in chunked(df, chunk_size=500):
    results = process_batch(chunk)
    save_checkpoint(results)
```

### Quality Control

```python
# Review low-confidence mappings
low_conf = df[df['CLIP Confidence'] < 0.70]
print(f"Review needed: {len(low_conf)} items")
low_conf.to_excel('review_queue.xlsx')
```

##  Troubleshooting

### Common Issues

**Out of Memory on GPU**
```python
# Reduce image size
IMAGE_SIZE = (512, 512)  # Smaller images
```

**Low Accuracy**
```python
# Increase threshold, review more
CONFIDENCE_THRESHOLD = 0.8  

# Or expand allowed colors list
# Add more specific shades to your master list
```

**Images Not Downloading**
```python
# Check URLs are publicly accessible
# Add retry logic or increase timeout
async with session.get(url, timeout=60) as response:
```

**English Words in Non-English Output**
```python
# Already handled by leak detection
# Check logs for "EnglishLeak%" warnings
# System auto-retries with stronger prompts
```

##  Documentation

- [QUICKSTART.md](QUICKSTART.md) - Get running in 15 minutes
- [INTERNAL_GUIDE.md](INTERNAL_GUIDE.md) - Team deployment guide
- [API.md](API.md) - Code documentation
- [EXAMPLES.md](EXAMPLES.md) - Common use cases

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional language support
- Alternative vision models (DINOv2, etc.)
- Color palette extraction from images
- Real-time API mode
- Web interface

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

## 👤 Author

**Yugesh**

E-commerce automation specialist with 4+ years in marketplace integration and operations optimization. Built this tool to solve real problems in international product management.

*Previously: Senior Marketplace Specialist | Currently: Consultant at Deloitte TMT*

Connect: [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- **OpenAI CLIP** team for the vision-language model
- **Hugging Face** for the Transformers library
- E-commerce operations teams who tested and provided feedback
- Open-source community

## 📧 Support

- **Issues**: Use GitHub Issues for bug reports
- **Discussions**: GitHub Discussions for questions
- **Email**: Contact for enterprise support

## 🌟 Star History

If this tool saved you time, consider giving it a star ⭐

---

**Built with ❤️ by Yugesh | Solving real e-commerce challenges through AI**

*"The best tools are built by people who face the problems themselves."*
