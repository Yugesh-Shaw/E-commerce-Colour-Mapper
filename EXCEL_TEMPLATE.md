# Excel Template Structure - Color Mapper

*Excel format specification - Designed by Yugesh*

## 📋 Required Format

Your Excel workbook must have **exactly 2 sheets**:

---

## Sheet 1: "Postman - Colour Code"

**Purpose**: Your allowed marketplace color codes (master list)

**Required Columns:**
1. `values.value.label` - Human-readable color name
2. `values.value.code` - Standardized code

**Example:**

| values.value.label | values.value.code |
|-------------------|-------------------|
| Navy Blue | NAVY_BLUE |
| Sky Blue | SKY_BLUE |
| Royal Blue | ROYAL_BLUE |
| Forest Green | FOREST_GREEN |
| Olive Green | OLIVE_GREEN |
| Sage Green | SAGE_GREEN |
| Crimson Red | CRIMSON_RED |
| Burgundy Red | BURGUNDY_RED |
| Cherry Red | CHERRY_RED |

**Notes:**
- This is your "allowed colors" master list
- Add all possible colors your marketplace supports
- More colors = better matching options
- Keep names clear and descriptive

---

## Sheet 2: "Colour Mapping"

**Purpose**: Products whose colors need to be mapped

**Required Columns:**
1. `colour` - Product color description (any language)
2. `Image Link` - Product image URL (optional but recommended)

**Example:**

| colour | Image Link |
|--------|------------|
| marine foncé / 24 | https://cdn.example.com/product1.jpg |
| vert olive | https://cdn.example.com/product2.jpg |
| rouge bordeaux / XL | https://cdn.example.com/product3.jpg |
| blau / M | https://cdn.example.com/product4.jpg |
| olivgrün camo | https://cdn.example.com/product5.jpg |

**Notes:**
- `colour` can be in ANY language (French, German, Italian, etc.)
- Can include size info (e.g., "/ 24", "/ XL") - will be parsed
- `Image Link` is optional but **improves accuracy by 10-15%**
- Images should be publicly accessible URLs

---

## Output Format

After processing, Sheet 2 will have **3 new columns**:

| colour | Image Link | **Mapped Colour Code** | **CLIP Suggestions** | **CLIP Confidence** |
|--------|------------|----------------------|---------------------|-------------------|
| marine foncé / 24 | https://... | NAVY_BLUE | Navy Blue | 0.89 |
| vert olive | https://... | OLIVE_GREEN | Olive Green | 0.82 |
| rouge bordeaux | https://... | BURGUNDY_RED | Burgundy Red | 0.73 |

**Column Descriptions:**
- **Mapped Colour Code**: The final matched code from your master list
- **CLIP Suggestions**: The human-readable color name that was matched
- **CLIP Confidence**: Confidence score (0.0 to 1.0)

---

## 📝 Creating Your Template

### Step 1: Create Workbook

1. Open Excel/Google Sheets
2. Create new workbook
3. Save as `Colour_Map_Template.xlsx`

### Step 2: Setup Sheet 1

1. Rename first sheet to: **"Postman - Colour Code"**
2. Add headers:
   - Column A: `values.value.label`
   - Column B: `values.value.code`
3. Fill with your marketplace's allowed colors

**Pro Tip**: Get this list from your marketplace API documentation or product management team.

### Step 3: Setup Sheet 2

1. Create second sheet named: **"Colour Mapping"**
2. Add headers:
   - Column A: `colour`
   - Column B: `Image Link`
3. Paste your product data

**Pro Tip**: Export from your product database or PIM system.

---

## 🎯 Best Practices

### For "Postman - Colour Code" Sheet

✅ **DO:**
- Include all possible color variations
- Use clear, descriptive names
- Group similar colors (all blues together)
- Keep codes consistent (UPPER_CASE_SNAKE_CASE)

❌ **DON'T:**
- Use duplicate codes
- Mix naming conventions
- Leave empty rows
- Include special characters in codes

### For "Colour Mapping" Sheet

✅ **DO:**
- Clean data before import (remove extra spaces)
- Use high-quality image URLs
- Include as much text context as possible
- Test with small batch first (10-20 items)

❌ **DON'T:**
- Use broken/private image URLs
- Mix multiple colors in one cell
- Include pricing or unrelated data
- Process without testing first

---

## 📊 Example Files

### Minimal Test File (5 items)

**Sheet 1: Postman - Colour Code**
```
Navy Blue,NAVY_BLUE
Black,BLACK
White,WHITE
Red,RED
Green,GREEN
```

**Sheet 2: Colour Mapping**
```
colour,Image Link
navy,https://example.com/navy.jpg
black / M,https://example.com/black.jpg
white,https://example.com/white.jpg
```

### Production File (1000+ items)

Same structure, just more rows. Recommended workflow:
1. Process in batches of 500
2. Review each batch
3. Merge results

---

## 🔍 Data Quality Tips

### Getting Better Results

**Improve Accuracy:**
1. **Better Images**: High-res, good lighting, clear color
2. **Clean Text**: Remove size codes, keep color names
3. **More Context**: "navy blue jacket" better than "blue"
4. **Comprehensive List**: More allowed colors = better matching

**Common Issues:**

| Issue | Solution |
|-------|----------|
| Too many "No Match" | Expand allowed colors list |
| Wrong blue shades | Add more blue variations to master list |
| Low confidence | Check image quality, add more context |
| Mixed languages | Already handled! Just run as-is |

---

## 💡 Pro Tips

### From Yugesh (Creator)

> "After processing 2,500+ colors, I learned that image quality matters more than you think. A clear product photo can turn a 0.65 confidence into 0.85+."

**Key Insights:**
1. **Master List is Critical**: Spend time building comprehensive allowed colors
2. **Images Matter**: 10-15% accuracy boost with good images
3. **Batch Processing**: Do 100 at a time, review, adjust
4. **Language Agnostic**: Don't worry about mixed languages - it handles them
5. **Context Helps**: "dark navy blue" better than just "dark"

---

## 📁 File Location

**Recommended Google Drive structure:**

```
/MyDrive/
  └── Color Map/
      ├── Colour_Map_Template.xlsx     ← Your input
      ├── Output.xlsx                  ← Generated results
      └── Archive/
          ├── 2024-10-kiabi.xlsx
          └── 2024-11-obelink.xlsx
```

---

## 🚨 Common Mistakes to Avoid

1. **Wrong Sheet Names**: Must be exactly "Postman - Colour Code" and "Colour Mapping"
2. **Wrong Column Names**: Case-sensitive! Match exactly as shown
3. **Empty Allowed List**: Need at least 10-20 colors in master list
4. **Private Images**: URLs must be publicly accessible
5. **Special Characters**: Avoid in color codes (use underscores)

---

## ✅ Validation Checklist

Before running the mapper:

**Sheet 1 (Master List):**
- [ ] Named "Postman - Colour Code"
- [ ] Has columns: values.value.label, values.value.code
- [ ] At least 10 colors listed
- [ ] No duplicate codes
- [ ] No empty rows

**Sheet 2 (Products):**
- [ ] Named "Colour Mapping"
- [ ] Has columns: colour, Image Link
- [ ] Color descriptions present
- [ ] Image URLs accessible (test 2-3)
- [ ] No special formatting (bold, colors, etc.)

---

## 📞 Need Help?

**Template Issues:**
- Check column names are EXACT match (case-sensitive)
- Verify sheet names (no extra spaces)
- Ensure file is .xlsx format

**Data Issues:**
- Clean data before import
- Test with small batch first
- Review [QUICKSTART.md](QUICKSTART.md) for examples

---

*Template designed by Yugesh based on 2,500+ production mappings*
