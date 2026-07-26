"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SalesInvolvementType``."""

from typing import Literal, TypeAlias, cast

SalesInvolvementType: TypeAlias = Literal[
    "For Visibility Only",
    "Co-Sell",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SalesInvolvementType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SalesInvolvementType:
    return cast(SalesInvolvementType, data)
