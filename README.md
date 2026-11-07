# Security audit: efekrbas/guns.lol-username-checker

Date: 2026-11-07 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 1 issue(s): 1 critical.

## Findings

### 1. [CRITICAL] Command injection via shell=True

**CWE-78** | `gunslol.py` line 498

User input passed to a shell command. Attacker can execute arbitrary OS commands.

```
os.system("pause >nul")
```

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
---
