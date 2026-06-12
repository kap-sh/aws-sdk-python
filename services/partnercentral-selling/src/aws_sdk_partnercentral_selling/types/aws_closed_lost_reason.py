"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsClosedLostReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

AwsClosedLostReason: TypeAlias = Literal[
    "Administrative",
    "Business Associate Agreement",
    "Company Acquired/Dissolved",
    "Competitive Offering",
    "Customer Data Requirement",
    "Customer Deficiency",
    "Customer Experience",
    "Delay / Cancellation of Project",
    "Duplicate",
    "Duplicate Opportunity",
    "Executive Blocker",
    "Failed Vetting",
    "Feature Limitation",
    "Financial/Commercial",
    "Insufficient Amazon Value",
    "Insufficient AWS Value",
    "International Constraints",
    "Legal / Tax / Regulatory",
    "Legal Terms and Conditions",
    "Lost to Competitor",
    "Lost to Competitor - Google",
    "Lost to Competitor - Microsoft",
    "Lost to Competitor - Other",
    "Lost to Competitor - Rackspace",
    "Lost to Competitor - SoftLayer",
    "Lost to Competitor - VMWare",
    "No Customer Reference",
    "No Integration Resources",
    "No Opportunity",
    "No Perceived Value of MP",
    "No Response",
    "Not Committed to AWS",
    "No Update",
    "On Premises Deployment",
    "Other",
    "Other (Details in Description)",
    "Partner Gap",
    "Past Due",
    "People/Relationship/Governance",
    "Platform Technology Limitation",
    "Preference for Competitor",
    "Price",
    "Product/Technology",
    "Product Not on AWS",
    "Security / Compliance",
    "Self-Service",
    "Technical Limitations",
    "Term Sheet Impasse",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Administrative",
        "Business Associate Agreement",
        "Company Acquired/Dissolved",
        "Competitive Offering",
        "Customer Data Requirement",
        "Customer Deficiency",
        "Customer Experience",
        "Delay / Cancellation of Project",
        "Duplicate",
        "Duplicate Opportunity",
        "Executive Blocker",
        "Failed Vetting",
        "Feature Limitation",
        "Financial/Commercial",
        "Insufficient Amazon Value",
        "Insufficient AWS Value",
        "International Constraints",
        "Legal / Tax / Regulatory",
        "Legal Terms and Conditions",
        "Lost to Competitor",
        "Lost to Competitor - Google",
        "Lost to Competitor - Microsoft",
        "Lost to Competitor - Other",
        "Lost to Competitor - Rackspace",
        "Lost to Competitor - SoftLayer",
        "Lost to Competitor - VMWare",
        "No Customer Reference",
        "No Integration Resources",
        "No Opportunity",
        "No Perceived Value of MP",
        "No Response",
        "Not Committed to AWS",
        "No Update",
        "On Premises Deployment",
        "Other",
        "Other (Details in Description)",
        "Partner Gap",
        "Past Due",
        "People/Relationship/Governance",
        "Platform Technology Limitation",
        "Preference for Competitor",
        "Price",
        "Product/Technology",
        "Product Not on AWS",
        "Security / Compliance",
        "Self-Service",
        "Technical Limitations",
        "Term Sheet Impasse",
    )
)


def serialize_aws_json_1_0(value: AwsClosedLostReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsClosedLostReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AwsClosedLostReason value: {data!r}")
    return cast(AwsClosedLostReason, data)
