"""Generated from Smithy shape ``com.amazonaws.wafv2#PositionalConstraint``."""

from typing import Literal, TypeAlias, cast

PositionalConstraint: TypeAlias = Literal[
    "EXACTLY",
    "STARTS_WITH",
    "ENDS_WITH",
    "CONTAINS",
    "CONTAINS_WORD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PositionalConstraint) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PositionalConstraint:
    return cast(PositionalConstraint, data)
