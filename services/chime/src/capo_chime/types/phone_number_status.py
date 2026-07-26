"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: PhoneNumberStatus) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberStatus:
    return cast(PhoneNumberStatus, data)
