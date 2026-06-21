"""Generated from Smithy shape ``com.amazonaws.lightsail#RecordState``."""

from typing import Literal, TypeAlias, cast

RecordState: TypeAlias = Literal[
    "Started",
    "Succeeded",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordState:
    return cast(RecordState, data)
