"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TriggerMode``."""

from typing import Literal, TypeAlias, cast

TriggerMode: TypeAlias = Literal[
    "ALWAYS",
    "RISING_EDGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TriggerMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TriggerMode:
    return cast(TriggerMode, data)
