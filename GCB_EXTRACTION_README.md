# Good Class Bungalow (GCB) Address Extraction Tool

This tool extracts all Good Class Bungalow addresses in Singapore using the OneMap API and saves them to a CSV file.

## About Good Class Bungalows (GCB)

Good Class Bungalows are exclusive residential areas in Singapore designated by the Urban Redevelopment Authority (URA). These are prestigious landed property areas with strict development guidelines. There are 39 designated GCB areas in Singapore.

## Features

- ✅ Extracts addresses from all 25+ known GCB areas in Singapore
- ✅ Uses Singapore's official OneMap API
- ✅ Saves results to a clean CSV file format
- ✅ Includes postal codes, coordinates, and building names
- ✅ No authentication required for OneMap API
- ✅ Respectful API usage with rate limiting

## Installation

### Prerequisites
- Python 3.7 or higher
- Internet connection to access OneMap API

### Setup

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests
```

## Usage

### Running the Main Script

To extract all GCB addresses and save to CSV:

```bash
python3 extract_gcb_addresses.py
```

This will:
1. Query the OneMap API for each GCB area
2. Extract all addresses found
3. Save results to `gcb_addresses.csv` in the current directory
4. Display a summary of results

### Testing with Mock Data

To verify the script works correctly without calling the API:

```bash
python3 test_gcb_extraction.py
```

This runs a mock test with sample data to verify the script structure is correct.

## Output Format

The generated CSV file (`gcb_addresses.csv`) contains the following columns:

| Column | Description |
|--------|-------------|
| GCB Area | The GCB area name (e.g., "Nassim Road") |
| Full Address | Complete address string |
| Postal Code | Singapore postal code |
| Building Name | Name of building (if applicable) |
| Road Name | Street name |
| Latitude | Latitude coordinate (WGS84) |
| Longitude | Longitude coordinate (WGS84) |
| X Coordinate | X coordinate (SVY21) |
| Y Coordinate | Y coordinate (SVY21) |

### Sample Output

```csv
GCB Area,Full Address,Postal Code,Building Name,Road Name,Latitude,Longitude,X Coordinate,Y Coordinate
Nassim Road,1 NASSIM ROAD SINGAPORE 258458,258458,NASSIM MANSION,NASSIM ROAD,1.30734,103.81796,28991.8304,32831.9224
Cluny Road,5 CLUNY ROAD SINGAPORE 259595,259595,,CLUNY ROAD,1.31349,103.81507,28735.0547,33512.8844
```

## GCB Areas Covered

The script searches the following GCB areas:

- Nassim Road
- Cluny Road
- Dalvey Road
- Ridley Park
- Queen Astrid Park
- Leedon Park
- Clementi Park
- Caldecott Hill
- Stevens Road
- Bukit Tunggal
- White House Park
- Chatsworth Park
- Tanglin Hill
- Goodwood Hill
- Cluny Park
- Ewart Park
- Swiss Club Road
- Sixth Avenue
- Raffles Park
- Bin Tong Park
- Grangeford Park
- Botanic Gardens
- Holland Road
- Cornwall Gardens
- Belmont Road

## API Information

This tool uses the OneMap API, Singapore's national map service:
- **Base URL**: `https://www.onemap.gov.sg/api/common/elastic/search`
- **Documentation**: https://www.onemap.gov.sg/docs/
- **No authentication required** for basic search
- **Free to use** for public data

## Customization

### Adding More Areas

To add additional GCB areas, edit the `GCB_AREAS` list in `extract_gcb_addresses.py`:

```python
GCB_AREAS = [
    "Nassim Road",
    "Cluny Road",
    # Add your areas here
    "Your Custom Area",
]
```

### Changing Output Filename

Modify the `save_to_csv()` call in the `main()` function:

```python
save_to_csv(addresses, "custom_filename.csv")
```

## Troubleshooting

### No results found
- Check your internet connection
- Verify OneMap API is accessible: https://www.onemap.gov.sg/
- Some GCB areas may have limited public address data

### API Rate Limiting
The script includes a 0.5-second delay between requests. If you encounter rate limiting:
- Increase the delay in the `time.sleep()` call
- Run the script during off-peak hours

### Connection Errors
If you get connection errors:
- Verify you can access https://www.onemap.gov.sg/ in your browser
- Check if you're behind a proxy or firewall
- Try running the script from a different network

## Notes

- The OneMap API returns publicly available address data
- Not all properties in GCB areas may be returned by the API
- Some GCB areas may have limited data availability
- Coordinates are provided in both WGS84 (Latitude/Longitude) and SVY21 (X/Y) formats

## License

This tool is provided as-is for educational and research purposes. Please respect the OneMap API terms of service and rate limits.

## Related Resources

- [OneMap API Documentation](https://www.onemap.gov.sg/docs/)
- [URA GCB Guidelines](https://www.ura.gov.sg/)
- [Singapore Land Authority](https://www.sla.gov.sg/)

## Support

For issues or questions about:
- **OneMap API**: Visit https://www.onemap.gov.sg/
- **This tool**: Open an issue in this repository
