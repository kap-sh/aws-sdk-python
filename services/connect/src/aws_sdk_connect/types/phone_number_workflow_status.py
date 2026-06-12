"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberWorkflowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

PhoneNumberWorkflowStatus: TypeAlias = Literal[
    "CLAIMED",
    "IN_PROGRESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLAIMED",
        "IN_PROGRESS",
        "FAILED",
    )
)


def serialize_json(value: PhoneNumberWorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> PhoneNumberWorkflowStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PhoneNumberWorkflowStatus value: {data!r}")
    return cast(PhoneNumberWorkflowStatus, data)
