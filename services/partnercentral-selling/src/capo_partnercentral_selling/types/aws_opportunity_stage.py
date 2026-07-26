"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityStage``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: AwsOpportunityStage) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsOpportunityStage:
    return cast(AwsOpportunityStage, data)
