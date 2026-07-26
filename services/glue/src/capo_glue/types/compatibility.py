"""Generated from Smithy shape ``com.amazonaws.glue#Compatibility``."""

from typing import Literal, TypeAlias, cast

Compatibility: TypeAlias = Literal[
    "NONE",
    "DISABLED",
    "BACKWARD",
    "BACKWARD_ALL",
    "FORWARD",
    "FORWARD_ALL",
    "FULL",
    "FULL_ALL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Compatibility) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Compatibility:
    return cast(Compatibility, data)
