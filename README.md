# Python Scripts Collection

Personal collection of Python scripts, automation tools, CTF utilities, and practice exercises.

## Repository Structure

```text
python-scripts/
├── A&D/
│   └── template_farm.py
└── fcc-cert/
    ├── 1-report-card.py
    └── 2-employee-profile-gen.py
```

---

## Contents

### 1. `A&D/` (Attack & Defense CTF)

Contains automated farming tools and templates for Attack & Defense CTF competitions.

* **`template_farm.py`**: Generic multi-threaded auto-farming script powered by `pwntools`. Automatically loops through target teams, executes service exploits, extracts flags via regex, filters out duplicates and self-targets, and submits flags to the scoring engine.

#### How to Use `template_farm.py`:

1. **Configure Targets & Own Service Protection**:
   ```python
   MY_TEAM = 1                          # Your team ID (will be excluded from attack)
   OWN_HOSTS = ["10.60.1.1"]            # Custom IP blacklist to prevent attacking own services
   TARGETS = [f"10.60.{t}.1" for t in range(1, 21) if t != MY_TEAM]
   ```

2. **Set Flag Pattern & Submitter**:
   ```python
   FLAG_REGEX = re.compile(r"[A-Za-z0-9_]{3,16}\{[A-Za-z0-9_+\-=/]{16,}\}")
   SUBMIT_MODE = "http_json"            # Options: "http_json", "http_form", "tcp"
   SUBMIT_URL = "http://10.10.0.1/api/v1/flags"
   SUBMIT_TOKEN = "YOUR_TEAM_TOKEN"
   ```

3. **Implement Exploit**:
   Put your exploit logic inside the `exploit(target)` function:
   * **Web/HTTP**: Send requests via `requests.Session()` and return response body.
   * **Binary/TCP**: Connect via `pwn.remote(host, port)` and return received data.

4. **Run the Farmer**:
   ```bash
   python3 A&D/template_farm.py
   ```

---

### 2. `fcc-cert/`

Practice exercises from the freeCodeCamp Python certification track:
* `1-report-card.py`: Formatting, f-strings, basic input/output.
* `2-employee-profile-gen.py`: Data type conversions, slicing, and validation.
