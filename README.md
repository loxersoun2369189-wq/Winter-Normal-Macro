

---

# Winter-Normal-Macro
An anime vanguards macro for the winter normal LTM mode

# What is this?
This just contains updated versions of the winter event.  
For the rest of the files download from:  
- https://mega.nz/file/CphzFRiR#s5_-7hDLLsRpXCn5DjvZ6p9ZT-V0tVR8_sHXh21uiZM
### MAKE SURE TO REMOVE THIS IN Tools\avMethods.py
```
print(reset_match())
```
# Recent updates

### Fixed stop/start key not stopping
### Added loop-wide lost detection
### Removed reset_mount() was useless
### Fixed retry breaking for some people, get new image [here](https://github.com/loxerex/Winter-Normal-Macro/blob/main/Resources/Winter/DetectLoss.png)
### Full numbis support + auto start
```python
AUTO_START = True # if true upon failure it will auto restart, this also starts the macro when you launch the script
USE_NIMBUS = True # Use the nimbus cloud instead of newsman (more consistent + better)
detect_loss() # detects + restarts 
```

---

## Common Fixes
Mega downloads can occasionally corrupt files, which breaks either **Python** or **Tesseract**.

### Tesseract issues
If Tesseract stops working or the macro can’t detect text:

- Re‑download the files and unzip again, **or**
- Install a clean version of Tesseract from:  
  https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0  
- Clear the old Tesseract folder before installing
- Optionally add the **Tesseract directory** (not the exe) to your system PATH

### Python issues
If Python fails to run or packages are missing:

- Install a clean Python **3.13.11**
- Install the required packages listed here:  
  https://pastebin.com/mS2xFd3m

---
