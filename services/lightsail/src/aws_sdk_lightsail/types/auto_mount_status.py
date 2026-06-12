"""Generated from Smithy shape ``com.amazonaws.lightsail#AutoMountStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

AutoMountStatus: TypeAlias = Literal[
    "Failed",
    "Pending",
    "Mounted",
    "NotMounted",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Failed",
        "Pending",
        "Mounted",
        "NotMounted",
    )
)


def serialize_aws_json_1_1(value: AutoMountStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMountStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMountStatus value: {data!r}")
    return cast(AutoMountStatus, data)
