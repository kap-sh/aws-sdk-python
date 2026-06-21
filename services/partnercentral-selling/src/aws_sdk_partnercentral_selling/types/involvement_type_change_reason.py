"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#InvolvementTypeChangeReason``."""

from typing import Literal, TypeAlias, cast

InvolvementTypeChangeReason: TypeAlias = Literal[
    "Expansion Opportunity",
    "Change in Deal Information",
    "Customer Requested",
    "Technical Complexity",
    "Risk Mitigation",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvolvementTypeChangeReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InvolvementTypeChangeReason:
    return cast(InvolvementTypeChangeReason, data)
