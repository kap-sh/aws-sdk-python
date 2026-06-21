"""Generated from Smithy shape ``com.amazonaws.b2bi#X12SplitBy``."""

from typing import Literal, TypeAlias, cast

X12SplitBy: TypeAlias = Literal[
    "NONE",
    "TRANSACTION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12SplitBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> X12SplitBy:
    return cast(X12SplitBy, data)
