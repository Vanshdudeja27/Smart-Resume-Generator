import requests

def scrape_jobs(keyword="Data Scientist", location="Remote", num_jobs=5):
    """
    Fetches job listings from Remotive.io API based on keyword and location.

    Args:
        keyword (str): Job search keyword (e.g., "Data Scientist").
        location (str): Job location preference (e.g., "Remote").
        num_jobs (int): Maximum number of jobs to return.

    Returns:
        List[dict]: A list of job dictionaries containing title, company, description, and apply link.
    """
    url = f"https://remotive.io/api/remote-jobs?search={keyword}"
    print(f"[INFO] Fetching jobs from: {url}")

    try:
        response = requests.get(url, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed: {e}")
        return []

    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch jobs. Status code: {response.status_code}")
        return []

    try:
        data = response.json()
    except Exception as e:
        print(f"[ERROR] Could not decode JSON: {e}")
        print("Raw response text preview:\n", response.text[:300])
        return []

    jobs_raw = data.get("jobs", [])
    if not jobs_raw:
        print("[INFO] No jobs found for the given keyword.")
        return []

    job_listings = []
    for job in jobs_raw[:num_jobs]:
        job_listings.append({
            "title": job.get("title", "No Title"),
            "company": job.get("company_name", "Unknown Company"),
            "description": job.get("description", "No Description"),
            "apply_link": job.get("url", "#")
        })

    print(f"[INFO] Found {len(job_listings)} job(s) for '{keyword}' in '{location}'")
    return job_listings
