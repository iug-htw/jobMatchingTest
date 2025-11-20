from string import Template
import random
import json
import csv
import os

OUT_PATH = 'cv_records.csv'
field_names = [
    'cv_id',
    'name',
    'description',
    'gender',
    'ethnicity',
    'role',
    'domain',
]

def generate_dataset(data_dir='data_assets'):
    with open(os.path.join(data_dir, 'NAMES.json')) as f:
        names = json.load(f)
    with open(os.path.join(data_dir, 'ROLE_TO_DOMAIN.json')) as f:
        roles = json.load(f)
    with open(os.path.join(data_dir, 'COMPANIES_BY_DOMAIN.json')) as f:
        companies = json.load(f)
    with open(os.path.join(data_dir, 'SKILLS_BY_ROLE.json')) as f:
        skills = json.load(f)

    TEMPLATE = Template("$name - $role at $company, experienced in $skills.")

    count = 0
    out_file_exists = os.path.isfile(OUT_PATH)

    with open(OUT_PATH, 'w', newline='') as out_f:
        writer = csv.DictWriter(out_f, fieldnames=field_names)
        if not out_file_exists:
            writer.writeheader()

        for name_instance in names:
            name = name_instance['name']
            gender = name_instance['gender']
            ethnicity = name_instance['ethnicity']

            for role, domain in roles.items():
                company = random.choice(companies[domain])
                skill = skills[role]

                description = TEMPLATE.safe_substitute({
                    "name": name,
                    "role": role, 
                    "company": company,
                    "skills": skill
                })

                writer.writerow({
                    'cv_id': f"CV_{count}",
                    'name': name,
                    'description': description,
                    'gender': gender,
                    'ethnicity': ethnicity,
                    'role': role,
                    'domain': domain,
                })

                count += 1

    print(f"✅ Generated {count} instances.")
    print(f"Saved to {OUT_PATH}")
                