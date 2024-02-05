import random

from faker import Faker

fake = Faker()

def generate_company():
    return {
        "name": fake.company(),
        "mission": fake.bs(),
        "catch_phrase": fake.catch_phrase()
    }


if __name__ == '__main__':

    print("Generating fake data...")

    # Generate a limited set of companies
    companies = [generate_company() for _ in range(10)]
    company_names = [company["name"] for company in companies]

    print("I have just generated the following companies:")
    print(company_names)
