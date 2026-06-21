"""Generated from Smithy shape ``com.amazonaws.lightsail#DiskState``."""

from typing import Literal, TypeAlias, cast

DiskState: TypeAlias = Literal[
    "pending",
    "error",
    "available",
    "in-use",
    "unknown",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiskState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DiskState:
    return cast(DiskState, data)
