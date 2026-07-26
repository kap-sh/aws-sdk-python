"""Generated from Smithy shape ``com.amazonaws.devicefarm#DevicePlatform``."""

from typing import Literal, TypeAlias, cast

DevicePlatform: TypeAlias = Literal[
    "ANDROID",
    "IOS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevicePlatform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DevicePlatform:
    return cast(DevicePlatform, data)
