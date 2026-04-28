#!/usr/bin/env python3
"""
ALUMINUM MINER - NO VALIDATION REQUIRED
Mines from ANY file - no format checking, just pure prime extraction
"""

import os
import time
import json
import pickle
from typing import List, Dict

class Node:
    __slots__ = ('data', 'next')
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data: int):
        node = Node(data)
        if not self.head:
            self.head = node
            self.size = 1
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        self.size += 1

    def to_list(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    def from_list(self, data_list):
        for data in data_list:
            self.append(data)

class PrimeTable:
    def __init__(self, id: int):
        self.id = id
        self.ll = LinkedList()
        self.verified = False

# ========== PRIME TESTING ==========
def is_prime(n: int) -> bool:
    """Simple but fast prime test for 32-bit numbers"""
    if n < 2:
        return False
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    
    # Check divisibility by numbers 6k±1
    i = 7
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# ========== MAIN MINER - NO VALIDATION ==========
def mine_from_file(filepath: str):
    """Mine primes from ANY file - no validation, just read and mine"""
    
    num_tables = 50
    primes_per_table = 10_000_000
    target_total = num_tables * primes_per_table
    
    print(f"\n{'='*60}")
    print(f"🔨 ALUMINUM MINER - NO VALIDATION MODE")
    print(f"File: {filepath}")
    print(f"Target: {target_total:,} primes from {num_tables} tables")
    print(f"{'='*60}\n")
    
    # Check file exists
    if not os.path.exists(filepath):
        print(f"❌ File not found: {filepath}")
        return
    
    # Get file size
    file_size = os.path.getsize(filepath)
    print(f"📁 File size: {file_size / 1024**3:.2f} GB")
    print(f"⛏️  Mining primes... (this will take a long time)\n")
    
    # Initialize
    tables = [PrimeTable(i) for i in range(num_tables)]
    current_table = 0
    chunks_read = 0
    primes_found = 0
    start_time = time.time()
    
    # Read file byte by byte
    with open(filepath, 'rb') as f:
        while True:
            # Read 4 bytes (32-bit integer)
            chunk = f.read(4)
            if len(chunk) < 4:
                break  # End of file
            
            chunks_read += 1
            num = int.from_bytes(chunk, 'little')
            
            # Test if prime
            if is_prime(num):
                tables[current_table].ll.append(num)
                primes_found += 1
                
                # Check if current table is complete
                if tables[current_table].ll.size >= primes_per_table:
                    print(f"✅ TABLE {current_table} COMPLETE! ({tables[current_table].ll.size:,} primes)")
                    tables[current_table].verified = True
                    current_table += 1
                    
                    # All tables done?
                    if current_table >= num_tables:
                        print(f"\n🎉 ALL {num_tables} TABLES COMPLETE!")
                        break
                
                # Progress update every 1000 primes
                if primes_found % 1000 == 0:
                    elapsed = time.time() - start_time
                    rate = primes_found / elapsed
                    eta = (target_total - primes_found) / rate
                    print(f"   Primes: {primes_found:,}/{target_total:,} ({primes_found/target_total*100:.2f}%) | Rate: {rate:.1f}/sec | ETA: {eta/3600:.1f}h")
    
    # Results
    elapsed = time.time() - start_time
    total_primes = sum(t.ll.size for t in tables)
    verified_count = sum(1 for t in tables if t.verified)
    
    result = {
        "file": filepath,
        "file_size_gb": round(file_size / 1024**3, 2),
        "chunks_read": chunks_read,
        "target_tables": num_tables,
        "completed_tables": verified_count,
        "total_primes": total_primes,
        "duration_seconds": round(elapsed),
        "duration_hours": round(elapsed / 3600, 1),
        "avg_rate": round(total_primes / elapsed, 2),
        "status": "COMPLETE" if verified_count == num_tables else "PARTIAL",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Save results
    output_file = f"mining_result_{int(time.time())}.json"
    with open(output_file, 'w') as f:
        json.dump(result, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"📊 RESULTS")
    print(f"{'='*60}")
    print(json.dumps(result, indent=2))
    print(f"\n💾 Saved to: {output_file}")
    
    return result

# ========== SCANNER ==========
def scan_for_files():
    """Find large files on system"""
    print("\n🔍 SCANNING FOR LARGE FILES...\n")
    
    paths_to_scan = [
        os.path.expandvars(r"%localappdata%\NVIDIA\DXCache"),
        os.path.expandvars(r"%localappdata%\NVIDIA\GLCache"),
        os.path.expandvars(r"%localappdata%\AMD\DxCache"),
        r"C:\Program Files (x86)\Steam\steamapps\shadercache",
        os.path.expandvars(r"%userprofile%\Downloads"),
        os.path.expandvars(r"%userprofile%\Documents"),
    ]
    
    found_files = []
    
    for path in paths_to_scan:
        if os.path.exists(path):
            print(f"📁 Scanning: {path}")
            for root, dirs, files in os.walk(path):
                for file in files:
                    try:
                        full_path = os.path.join(root, file)
                        size_mb = os.path.getsize(full_path) / 1024**2
                        if size_mb > 50:  # Files larger than 50MB
                            found_files.append((full_path, size_mb))
                    except:
                        pass
    
    # Sort by size
    found_files.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\n{'='*60}")
    print(f"📁 FOUND {len(found_files)} LARGE FILES:")
    print(f"{'='*60}\n")
    
    for i, (path, size_mb) in enumerate(found_files[:20], 1):
        print(f"{i}. {size_mb:.0f}MB - {os.path.basename(path)}")
        print(f"   {path}\n")
    
    return [path for path, _ in found_files]

# ========== MAIN ==========
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("="*60)
        print("🔨 ALUMINUM MINER - Prime Extractor")
        print("="*60)
        print("\nUSAGE:")
        print("   python aluminum_miner.py [FILE_PATH]     - Mine primes from a file")
        print("   python aluminum_miner.py --scan          - Find large files to mine")
        print("\nEXAMPLE:")
        print(f"   python aluminum_miner.py \"C:\\Users\\{os.getlogin()}\\AppData\\Local\\NVIDIA\\DXCache\\yourfile.nvph\"")
        print("\nTIP: Run --scan first to find files")
        sys.exit(0)
    
    if sys.argv[1] == "--scan":
        scan_for_files()
    else:
        filepath = sys.argv[1]
        mine_from_file(filepath)
