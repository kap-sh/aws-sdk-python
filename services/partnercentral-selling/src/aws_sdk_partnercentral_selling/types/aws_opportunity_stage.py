"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityStage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

AwsOpportunityStage: TypeAlias = Literal[
    "Not Started",
    "In Progress",
    "Prospect",
    "Engaged",
    "Identified",
    "Qualify",
    "Research",
    "Seller Engaged",
    "Evaluating",
    "Seller Registered",
    "Term Sheet Negotiation",
    "Contract Negotiation",
    "Onboarding",
    "Building Integration",
    "Qualified",
    "On-hold",
    "Technical Validation",
    "Business Validation",
    "Committed",
    "Launched",
    "Deferred to Partner",
    "Closed Lost",
    "Completed",
    "Closed Incomplete",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Not Started",
        "In Progress",
        "Prospect",
        "Engaged",
        "Identified",
        "Qualify",
        "Research",
        "Seller Engaged",
        "Evaluating",
        "Seller Registered",
        "Term Sheet Negotiation",
        "Contract Negotiation",
        "Onboarding",
        "Building Integration",
        "Qualified",
        "On-hold",
        "Technical Validation",
        "Business Validation",
        "Committed",
        "Launched",
        "Deferred to Partner",
        "Closed Lost",
        "Completed",
        "Closed Incomplete",
    )
)


def serialize_aws_json_1_0(value: AwsOpportunityStage) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsOpportunityStage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AwsOpportunityStage value: {data!r}")
    return cast(AwsOpportunityStage, data)
