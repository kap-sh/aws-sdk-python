"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityType``."""

from typing import Literal, TypeAlias, cast

OpportunityType: TypeAlias = Literal[
    "Net New Business",
    "Flat Renewal",
    "Expansion",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunityType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpportunityType:
    return cast(OpportunityType, data)
