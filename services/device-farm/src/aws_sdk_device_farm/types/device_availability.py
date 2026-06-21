"""Generated from Smithy shape ``com.amazonaws.devicefarm#DeviceAvailability``."""

from typing import Literal, TypeAlias, cast

DeviceAvailability: TypeAlias = Literal[
    "TEMPORARY_NOT_AVAILABLE",
    "BUSY",
    "AVAILABLE",
    "HIGHLY_AVAILABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceAvailability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeviceAvailability:
    return cast(DeviceAvailability, data)
