"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#RunType``."""

from typing import Literal, TypeAlias, cast

RunType: TypeAlias = Literal[
    "ON_DEMAND",
    "SCHEDULED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RunType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RunType:
    return cast(RunType, data)
