"""Generated from Smithy shape ``com.amazonaws.devicefarm#DevicePoolType``."""

from typing import Literal, TypeAlias, cast

DevicePoolType: TypeAlias = Literal[
    "CURATED",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevicePoolType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DevicePoolType:
    return cast(DevicePoolType, data)
