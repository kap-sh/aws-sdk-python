"""Generated from Smithy shape ``com.amazonaws.connect#DeviceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

DeviceType: TypeAlias = Literal[
    "GCM",
    "APNS",
    "APNS_SANDBOX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GCM",
        "APNS",
        "APNS_SANDBOX",
    )
)


def serialize_json(value: DeviceType) -> str:
    return value


def deserialize_json(data: str) -> DeviceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceType value: {data!r}")
    return cast(DeviceType, data)
