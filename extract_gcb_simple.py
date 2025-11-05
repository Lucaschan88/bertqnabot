"""
Quick Start Example - Extract GCB Addresses
This is a simplified version for easy understanding and modification
"""

import requests
import csv

def get_addresses_from_onemap(search_term):
    """Search OneMap API for addresses"""
    url = "https://www.onemap.gov.sg/api/common/elastic/search"
    params = {
        "searchVal": search_term,
        "returnGeom": "Y",
        "getAddrDetails": "Y",
        "pageNum": 1
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except Exception as e:
        print(f"Error: {e}")
        return []


def main():
    # List of GCB areas to search
    gcb_areas = [
        "Nassim Road",
        "Cluny Road",
        "Dalvey Road",
        # Add more areas as needed
    ]
    
    all_results = []
    
    print("Extracting GCB addresses...")
    for area in gcb_areas:
        print(f"Searching: {area}")
        results = get_addresses_from_onemap(area)
        
        for item in results:
            all_results.append({
                "area": area,
                "address": item.get("ADDRESS", ""),
                "postal": item.get("POSTAL", ""),
                "latitude": item.get("LATITUDE", ""),
                "longitude": item.get("LONGITUDE", "")
            })
    
    # Save to CSV
    if all_results:
        with open("gcb_simple.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["area", "address", "postal", "latitude", "longitude"])
            writer.writeheader()
            writer.writerows(all_results)
        
        print(f"\n✓ Saved {len(all_results)} addresses to 'gcb_simple.csv'")
    else:
        print("\n⚠ No addresses found")


if __name__ == "__main__":
    main()
