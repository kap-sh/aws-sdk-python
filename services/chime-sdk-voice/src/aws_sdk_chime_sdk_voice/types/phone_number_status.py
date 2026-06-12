"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

PhoneNumberStatus: TypeAlias = Literal[
    "Cancelled",
    "PortinCancelRequested",
    "PortinInProgress",
    "AcquireInProgress",
    "AcquireFailed",
    "Unassigned",
    "Assigned",
    "ReleaseInProgress",
    "DeleteInProgress",
    "ReleaseFailed",
    "DeleteFailed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Cancelled",
        "PortinCancelRequested",
        "PortinInProgress",
        "AcquireInProgress",
        "AcquireFailed",
        "Unassigned",
        "Assigned",
        "ReleaseInProgress",
        "DeleteInProgress",
        "ReleaseFailed",
        "DeleteFailed",
    )
)


def serialize_json(value: PhoneNumberStatus) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneNumberStatus value: {data!r}")
    return cast(PhoneNumberStatus, data)
