"""Generated from Smithy shape ``com.amazonaws.iotevents#InputStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_events.errors import DeserializationError

InputStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "ACTIVE",
        "DELETING",
    )
)


def serialize_json(value: InputStatus) -> str:
    return value


def deserialize_json(data: str) -> InputStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputStatus value: {data!r}")
    return cast(InputStatus, data)
