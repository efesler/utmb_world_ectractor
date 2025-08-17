# UTMB World Race Data Extractor

A Python script to extract runner data from UTMB World race results and export to CSV format.

## Features

- Fetches race data from UTMB World API
- Extracts runner information (name, firstname, race time)
- Accurately parses names using uppercase lastname pattern
- Exports data to CSV format with proper UTF-8 encoding

## Requirements

- Python 3.6+
- requests library

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install requests
   ```

## Usage

Run the script:
```bash
python utmb_world_extractor.py
```

The script will:
1. Fetch race data from the UTMB API
2. Parse runner information
3. Save results to `utmb_results.csv`

## Output Format

The CSV file contains the following columns:
- `name`: Runner's lastname (in uppercase)
- `firstname`: Runner's firstname(s)
- `time`: Race completion time

## Configuration

The script is currently configured for:
- Race: 80K OSO
- Tenant: quitobyutmb_2025

To modify for different races, update the URL and headers in the `fetch_utmb_data()` function.

## License

MIT License - see LICENSE file for details.