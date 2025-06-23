import argparse
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

def main():
    parser = argparse.ArgumentParser(description="Log a fiber splice")
    parser.add_argument("--crew", required=True)
    parser.add_argument("--segment", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--timestamp", required=True)
    parser.add_argument("--notes", default="")

    args = parser.parse_args()
    payload = {
        "crew_name": args.crew,
        "segment_id": args.segment,
        "splice_type": args.type,
        "timestamp": args.timestamp,
        "notes": args.notes
    }

    resp = requests.post(f"{API_URL}/api/splice", json=payload)
    print(resp.json())

if __name__ == "__main__":
    main()
