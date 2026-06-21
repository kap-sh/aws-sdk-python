"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberWorkflowStatus``."""

from typing import Literal, TypeAlias, cast

PhoneNumberWorkflowStatus: TypeAlias = Literal[
    "CLAIMED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberWorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberWorkflowStatus:
    return cast(PhoneNumberWorkflowStatus, data)
