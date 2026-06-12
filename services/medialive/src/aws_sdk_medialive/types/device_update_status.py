"""Generated from Smithy shape ``com.amazonaws.medialive#DeviceUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The status of software on the input device."""
DeviceUpdateStatus: TypeAlias = Literal[
    "UP_TO_DATE",
    "NOT_UP_TO_DATE",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UP_TO_DATE",
        "NOT_UP_TO_DATE",
        "UPDATING",
    )
)


def serialize_json(value: DeviceUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> DeviceUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeviceUpdateStatus value: {data!r}")
    return cast(DeviceUpdateStatus, data)
