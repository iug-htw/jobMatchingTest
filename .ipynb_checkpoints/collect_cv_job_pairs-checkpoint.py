import pandas as pd

def collect_cv_job_pairs(cv_df, job_df):
    cv_id_to_idx = dict(zip(cv_df["cv_id"], range(len(cv_df))))
    job_id_to_idx = dict(zip(job_df["job_id"], range(len(job_df))))

    pairs = []  # (cv_id, job_id)

    for _, cv in cv_df.iterrows():
        role = cv["role"]

        # jobs with the same role (domain is only on job_records.csv)
        matched_jobs = job_df[job_df["role"] == role]

        for _, job in matched_jobs.iterrows():
            pairs.append((cv["cv_id"], job["job_id"]))

    print(f"Total matched pairs: {len(pairs)}")

    return pairs