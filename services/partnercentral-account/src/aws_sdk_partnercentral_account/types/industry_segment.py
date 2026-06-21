"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#IndustrySegment``."""

from typing import Literal, TypeAlias, cast

IndustrySegment: TypeAlias = Literal[
    "AGRICULTURE_MINING",
    "BIOTECHNOLOGY",
    "BUSINESS_CONSUMER_SERVICES",
    "BUSINESS_SERV",
    "COMMUNICATIONS",
    "COMPUTER_HARDWARE",
    "COMPUTERS_ELECTRONICS",
    "COMPUTER_SOFTWARE",
    "CONSUMER_GOODS",
    "CONSUMER_RELATED",
    "EDUCATION",
    "ENERGY_UTILITIES",
    "FINANCIAL_SERVICES",
    "GAMING",
    "GOVERNMENT",
    "GOVERNMENT_EDUCATION_PUBLIC_SERVICES",
    "HEALTHCARE",
    "HEALTHCARE_PHARMACEUTICALS_BIOTECH",
    "INDUSTRIAL_ENERGY",
    "INTERNET_SPECIFIC",
    "LIFE_SCIENCES",
    "MANUFACTURING",
    "MEDIA_ENTERTAINMENT_LEISURE",
    "MEDIA_ENTERTAINMENT",
    "MEDICAL_HEALTH",
    "NON_PROFIT_ORGANIZATION",
    "OTHER",
    "PROFESSIONAL_SERVICES",
    "REAL_ESTATE_CONSTRUCTION",
    "RETAIL",
    "RETAIL_WHOLESALE_DISTRIBUTION",
    "SEMICONDUCTOR_ELECTR",
    "SOFTWARE_INTERNET",
    "TELECOMMUNICATIONS",
    "TRANSPORTATION_LOGISTICS",
    "TRAVEL_HOSPITALITY",
    "WHOLESALE_DISTRIBUTION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IndustrySegment) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IndustrySegment:
    return cast(IndustrySegment, data)
