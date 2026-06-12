"""Generated from Smithy shape ``com.amazonaws.devicefarm#DevicePlatform``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

DevicePlatform: TypeAlias = Literal[
    "ANDROID",
    "IOS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANDROID",
        "IOS",
    )
)


def serialize_aws_json_1_1(value: DevicePlatform) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DevicePlatform:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DevicePlatform value: {data!r}")
    return cast(DevicePlatform, data)
