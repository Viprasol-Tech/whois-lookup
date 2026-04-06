# Whois Lookup

Perform WHOIS lookups

## Features

- Zero external dependencies (stdlib only)
- Easy-to-use CLI interface
- Professional Python implementation
- MIT licensed

## Installation

```bash
pip install -e .
```

Or clone and install:

```bash
git clone https://github.com/Viprasol-Tech/whois-lookup
cd whois-lookup
pip install -e .
```

## Usage

### Python

```python
from whois_lookup import WhoisLookup

result = WhoisLookup.process("data")
print(result)
```

### CLI

```bash
python -m whois_lookup "your input here"
```

## Documentation

See the source code and docstrings for detailed API documentation.

## License

MIT License - see LICENSE file for details

## About

Part of Viprasol Utilities: https://viprasol.com

Created by Viprasol - Building AI-focused tools for developers.
