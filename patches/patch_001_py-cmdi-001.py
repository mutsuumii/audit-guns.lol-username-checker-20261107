# Command injection via shell=True
# CWE-78 | Severity: CRITICAL
# File: gunslol.py line 498

**Risk:** User input passed to a shell command. Attacker can execute arbitrary OS commands.

**Fix:** Use subprocess.run(['cmd', arg], shell=False). Never build shell strings from input.
