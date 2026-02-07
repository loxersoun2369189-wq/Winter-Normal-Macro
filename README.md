

---

# Winter-Normal-Macro
An anime vanguards macro for the winter normal LTM mode

# What is this?
This just contains updated versions of the winter event.  
For the rest of the files download from:  
https://mega.nz/file/C8p1nSpL#c_jFD9UViHjo4eYiVqW8Ep3nUB5L-e7x-f_rWsivvFA

# Recent updates

### Fixed stop/start key not stopping

### Full numbis support + auto start
```python
AUTO_START = True # if true upon failure it will auto restart, this also starts the macro when you launch the script
USE_NIMBUS = True # Use the nimbus cloud instead of newsman (more consistent + better)
```

### Added loop-wide lost detection
Restarts program upon lost + resets the mount too.

```python
detect_loss() # detects + restarts 
reset_mount() # resets the mount state to unmounted
```
