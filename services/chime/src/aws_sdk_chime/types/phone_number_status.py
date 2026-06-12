"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

PhoneNumberStatus: TypeAlias = Literal[
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
