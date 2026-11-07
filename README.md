# SecureForge Semgrep Detection Lab

This repository contains deliberately vulnerable examples for local scanner validation.
**Never deploy these examples or use their patterns in production.**

Expected custom-rule detections include SQL interpolation, shell execution, unsafe pickle/YAML deserialization, MD5, disabled TLS verification, hardcoded password-like values, JavaScript `innerHTML`, `document.write`, and `eval`.

`safe_examples.py` provides negative examples for parameterized SQL and SHA-256. A negative example is not a proof of general safety; it only checks that these particular safe patterns do not trigger the custom rules.
