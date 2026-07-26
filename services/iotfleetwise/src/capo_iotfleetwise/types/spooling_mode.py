"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SpoolingMode``."""

from typing import Literal, TypeAlias, cast

SpoolingMode: TypeAlias = Literal[
    "OFF",
    "TO_DISK",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SpoolingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SpoolingMode:
    return cast(SpoolingMode, data)
