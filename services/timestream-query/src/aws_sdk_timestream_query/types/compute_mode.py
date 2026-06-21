"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ComputeMode``."""

from typing import Literal, TypeAlias, cast

ComputeMode: TypeAlias = Literal[
    "ON_DEMAND",
    "PROVISIONED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComputeMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComputeMode:
    return cast(ComputeMode, data)
