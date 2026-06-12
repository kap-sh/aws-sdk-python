"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeviceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkmanager.errors import DeserializationError

DeviceState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "DELETING",
        "UPDATING",
    )
)


def serialize_json(value: DeviceState) -> str:
    return value


def deserialize_json(data: str) -> DeviceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceState value: {data!r}")
    return cast(DeviceState, data)
