import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import re
import csv
import json
import os

# Struktur Data untuk Menyimpan Tautan
visited_links = set()
internal_links = set()
external_links = set()
broken_links = set()
metadata = {}

# Fungsi untuk Mengecek Validitas URL
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Fungsi untuk Mengecek Status HTTP Tautan
def check_link_status(url):
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code
    except requests.RequestException:                                                                                                                                                    return None

# Fungsi Utama untuk Scraping
def scrape_links(url, base_domain, depth=1, max_depth=2):
    if url in visited_links or depth > max_depth:
        return
    visited_links.add(url)

    try:
        # Mengambil Konten Halaman
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mengambil Metadata Halaman
        metadata[url] = {
            "title": soup.title.string if soup.title else "Tidak ada judul",
            "description": soup.find("meta", attrs={"name": "description"})["content"] if soup.find("meta", attrs={"name": "description"}) else "Tidak ada deskripsi"
        }

        # Mencari Semua Tautan
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            full_url = urljoin(url, href)  # Mengubah tautan relatif menjadi absolut

            if is_valid_url(full_url):
                if base_domain in full_url:  # Tautan internal
                    if full_url not in internal_links:
                        internal_links.add(full_url)
                        print(f"[INTERNAL] {full_url} (Status: {check_link_status(full_url)})")
                        scrape_links(full_url, base_domain, depth=depth+1, max_depth=max_depth)
                else:  # Tautan eksternal
                    if full_url not in external_links:
                        external_links.add(full_url)
                        print(f"[EXTERNAL] {full_url} (Status: {check_link_status(full_url)})")
            else:
                broken_links.add(full_url)
    except requests.RequestException as e:
        broken_links.add(url)
        print(f"[BROKEN] {url} - Error: {e}")

# Fungsi untuk Menyimpan Hasil ke Berbagai Format
def save_results():
    if not os.path.exists("output"):
        os.makedirs("output")

    # Simpan Tautan Internal dan Eksternal
    with open("output/links.json", "w", encoding="utf-8") as file:
        json.dump({
            "internal_links": list(internal_links),
            "external_links": list(external_links),
            "broken_links": list(broken_links),
            "metadata": metadata
        }, file, indent=4)

    with open("output/links.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "URL", "Status"])
        for link in internal_links:
            writer.writerow(["Internal", link, check_link_status(link)])
        for link in external_links:
            writer.writerow(["External", link, check_link_status(link)])
        for link in broken_links:
            writer.writerow(["Broken", link, "Failed"])

    print("\nHasil berhasil disimpan dalam folder 'output'.")

# Fungsi Utama
def main():
    print("=== LinkScraper Pro - Versi Canggih ===")
    domain = input("Masukkan domain (contoh: situs-penipu.com): ").strip()
    base_url = f"https://{domain}"
    base_domain = urlparse(base_url).netloc

    # Memulai Proses Scraping dengan Multi-threading
    print("\nSedang memproses tautan, harap tunggu...\n")
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(scrape_links, base_url, base_domain)

    # Menyimpan Hasil
    save_results()

    # Ringkasan
    print("\n=== Ringkasan Hasil ===")
    print(f"Total tautan internal: {len(internal_links)}")
    print(f"Total tautan eksternal: {len(external_links)}")
    print(f"Total tautan rusak: {len(broken_links)}")
    print("Metadata halaman berhasil diambil.")

if __name__ == "__main__":
    main()
