"""
Configuration Template for AI Color Mapper
Author: Yugesh
Copy this to config.py and update with your settings
"""

# ==================== FILE PATHS ====================

# Input Excel file path (your color data)
FILE_PATH = '/content/drive/MyDrive/Color Map/Colour_Map_Template.xlsx'

# Output file path (where results will be saved)
OUTPUT_FILE = '/content/drive/MyDrive/Color Map/Mapped_Colors_Output.xlsx'


# ==================== MODEL SETTINGS ====================

# Confidence threshold for auto-accepting matches
# Higher = more strict, more manual reviews
# Lower = more lenient, fewer manual reviews
CONFIDENCE_THRESHOLD = 0.7  # Recommended: 0.7

# Image processing size (pixels)
# Larger = better quality but slower and more memory
# Smaller = faster but may miss details
IMAGE_SIZE = (1000, 1000)  # Options: (512,512), (1000,1000), (1500,1500)

# Image enhancement factors
CONTRAST_ENHANCE = 1.2  # Contrast boost (1.0 = no change)
COLOR_ENHANCE = 1.2     # Color saturation boost (1.0 = no change)


# ==================== MATCHING SETTINGS ====================

# Maximum colors to consider in family-based matching
KEEP_TOP = 64  # Default: 64

# Minimum family subset size before fallback to full list
MIN_SIZE = 6  # Default: 6


# ==================== PERFORMANCE SETTINGS ====================

# Number of concurrent image downloads
# Higher = faster but more memory usage
MAX_CONCURRENT_DOWNLOADS = 10  # Default: 10

# Image download timeout (seconds)
DOWNLOAD_TIMEOUT = 30  # Default: 30


# ==================== QUALITY CONTROL ====================

# Minimum confidence for logging warnings
WARN_THRESHOLD = 0.6  # Items below this get warnings

# Auto-retry attempts for failed downloads
MAX_RETRIES = 3  # Default: 3


# ==================== LANGUAGE SETTINGS ====================

# Supported language families (already built-in)
SUPPORTED_LANGUAGES = [
    'English', 'French', 'German', 
    'Italian', 'Polish', 'Spanish'
]

# Add custom color family if needed
# Example:
# CUSTOM_COLORS = {
#     "teal": {
#         "en": ["teal", "turquoise", "aqua"],
#         "fr": ["sarcelle", "turquoise"],
#     }
# }


# ==================== LOGGING ====================

# Log level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL = 'INFO'  # Default: INFO

# Save detailed logs to file?
SAVE_LOGS = True  # Default: True

# Log file path
LOG_FILE = '/content/drive/MyDrive/Color Map/color_mapping.log'


# ==================== ADVANCED SETTINGS ====================

# Use GPU if available?
USE_GPU = True  # Set False to force CPU

# CLIP model variant
CLIP_MODEL = "openai/clip-vit-base-patch32"  # Default model

# Batch size for CLIP processing
CLIP_BATCH_SIZE = 1  # Increase if you have more GPU memory


# ==================== PRESET CONFIGURATIONS ====================

# Uncomment one of these to use preset configurations

# PRESET 1: Fast Processing (Lower Accuracy)
# CONFIDENCE_THRESHOLD = 0.5
# IMAGE_SIZE = (512, 512)
# KEEP_TOP = 32

# PRESET 2: Balanced (Recommended)
# CONFIDENCE_THRESHOLD = 0.7
# IMAGE_SIZE = (1000, 1000)
# KEEP_TOP = 64

# PRESET 3: High Accuracy (Slower)
# CONFIDENCE_THRESHOLD = 0.85
# IMAGE_SIZE = (1500, 1500)
# KEEP_TOP = 128


# ==================== NOTES ====================
"""
Configuration Tips by Yugesh:

1. CONFIDENCE_THRESHOLD:
   - 0.5-0.6: Fast, more auto-accepts, review 30%
   - 0.7-0.8: Balanced, review 15-20% (recommended)
   - 0.85+: Strict, review 5-10%, very safe

2. IMAGE_SIZE:
   - (512, 512): Fast, good for bulk processing
   - (1000, 1000): Balanced, recommended default
   - (1500, 1500): Slow but best for complex colors

3. KEEP_TOP:
   - Lower (32): Faster, works for distinct colors
   - Medium (64): Balanced, handles most cases
   - Higher (128): Slower, best for subtle differences

4. Performance vs Quality:
   - Fast: threshold=0.5, size=512, keep_top=32
   - Balanced: threshold=0.7, size=1000, keep_top=64
   - Quality: threshold=0.85, size=1500, keep_top=128

5. Testing Workflow:
   - Start with 10 items, balanced settings
   - Check accuracy
   - Adjust threshold based on results
   - Scale up when satisfied

6. Production Use:
   - Process in batches of 500
   - Review flagged items after each batch
   - Track accuracy metrics
   - Adjust settings per marketplace

For questions: Check README.md or open GitHub issue
"""
