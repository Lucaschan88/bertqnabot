"""
Script to extract Good Class Bungalow (GCB) addresses in Singapore using OneMap API
and save them to a CSV file.

Good Class Bungalows are specific designated areas in Singapore where only landed properties
of a certain standard can be built.
"""

import requests
import csv
import time
from typing import List, Dict

# OneMap API endpoint
ONEMAP_SEARCH_URL = "https://www.onemap.gov.sg/api/common/elastic/search"

# List of known GCB areas in Singapore
GCB_AREAS = [
    "Nassim Road",
    "Cluny Road",
    "Dalvey Road",
    "Ridley Park",
    "Queen Astrid Park",
    "Leedon Park",
    "Clementi Park",
    "Caldecott Hill",
    "Stevens Road",
    "Bukit Tunggal",
    "White House Park",
    "Chatsworth Park",
    "Tanglin Hill",
    "Goodwood Hill",
    "Cluny Park",
    "Ewart Park",
    "Swiss Club Road",
    "Sixth Avenue",
    "Raffles Park",
    "Bin Tong Park",
    "Grangeford Park",
    "Botanic Gardens",
    "Holland Road",
    "Cornwall Gardens",
    "Belmont Road"
]


def search_onemap_address(search_term: str, return_geometry: str = "Y", get_address_details: str = "Y") -> Dict:
    """
    Search for addresses using OneMap API
    
    Args:
        search_term: The search term (e.g., road name, area name)
        return_geometry: Whether to return geometry (Y/N)
        get_address_details: Whether to get detailed address info (Y/N)
    
    Returns:
        Dict containing search results
    """
    params = {
        "searchVal": search_term,
        "returnGeom": return_geometry,
        "getAddrDetails": get_address_details,
        "pageNum": 1
    }
    
    try:
        response = requests.get(ONEMAP_SEARCH_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error searching for '{search_term}': {e}")
        return {"found": 0, "results": []}


def extract_gcb_addresses() -> List[Dict]:
    """
    Extract all Good Class Bungalow addresses from OneMap API
    
    Returns:
        List of dictionaries containing address information
    """
    all_addresses = []
    
    print("Extracting Good Class Bungalow addresses from OneMap API...")
    print(f"Searching {len(GCB_AREAS)} GCB areas\n")
    
    for idx, area in enumerate(GCB_AREAS, 1):
        print(f"[{idx}/{len(GCB_AREAS)}] Searching: {area}")
        
        # Search for the area
        result = search_onemap_address(area)
        
        if result.get("found", 0) > 0:
            results = result.get("results", [])
            print(f"  Found {len(results)} addresses")
            
            for address_data in results:
                address_info = {
                    "area": area,
                    "address": address_data.get("ADDRESS", ""),
                    "postal_code": address_data.get("POSTAL", ""),
                    "building_name": address_data.get("BUILDING", ""),
                    "road_name": address_data.get("ROAD_NAME", ""),
                    "latitude": address_data.get("LATITUDE", ""),
                    "longitude": address_data.get("LONGITUDE", ""),
                    "x_coordinate": address_data.get("X", ""),
                    "y_coordinate": address_data.get("Y", "")
                }
                all_addresses.append(address_info)
        else:
            print(f"  No results found")
        
        # Be respectful to the API - add a small delay
        time.sleep(0.5)
    
    return all_addresses


def save_to_csv(addresses: List[Dict], filename: str = "gcb_addresses.csv"):
    """
    Save addresses to a CSV file
    
    Args:
        addresses: List of address dictionaries
        filename: Output CSV filename
    """
    if not addresses:
        print("No addresses to save!")
        return False
    
    # Define CSV headers
    headers = [
        "GCB Area",
        "Full Address",
        "Postal Code",
        "Building Name",
        "Road Name",
        "Latitude",
        "Longitude",
        "X Coordinate",
        "Y Coordinate"
    ]
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=[
                "area", "address", "postal_code", "building_name", 
                "road_name", "latitude", "longitude", "x_coordinate", "y_coordinate"
            ])
            
            # Write header with friendly names
            csvfile.write(','.join(headers) + '\n')
            
            # Write data
            for addr in addresses:
                writer.writerow(addr)
        
        print(f"\n✓ Successfully saved {len(addresses)} addresses to '{filename}'")
        return True
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return False


def main():
    """Main function to extract GCB addresses and save to CSV"""
    print("=" * 70)
    print("Good Class Bungalow (GCB) Address Extraction Tool")
    print("Using OneMap API - Singapore's National Map Service")
    print("=" * 70)
    print()
    
    # Extract addresses
    addresses = extract_gcb_addresses()
    
    # Display summary
    print("\n" + "=" * 70)
    print(f"Extraction Complete!")
    print(f"Total addresses found: {len(addresses)}")
    print("=" * 70)
    
    if addresses:
        # Save to CSV
        save_to_csv(addresses)
        
        # Display sample of first 5 addresses
        print("\nSample of extracted addresses (first 5):")
        print("-" * 70)
        for i, addr in enumerate(addresses[:5], 1):
            print(f"{i}. {addr['address']}")
            if addr['postal_code']:
                print(f"   Postal Code: {addr['postal_code']}")
            print()
    else:
        print("No addresses were found. This might be due to API limitations or connectivity issues.")


if __name__ == "__main__":
    main()
