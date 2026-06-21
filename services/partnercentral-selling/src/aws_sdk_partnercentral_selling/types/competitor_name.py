"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CompetitorName``."""

from typing import Literal, TypeAlias, cast

CompetitorName: TypeAlias = Literal[
    "Oracle Cloud",
    "On-Prem",
    "Co-location",
    "Akamai",
    "AliCloud",
    "Google Cloud Platform",
    "IBM Softlayer",
    "Microsoft Azure",
    "Other- Cost Optimization",
    "No Competition",
    "*Other",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompetitorName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CompetitorName:
    return cast(CompetitorName, data)
