"""Generated from Smithy shape ``com.amazonaws.qbusiness#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ApplicationStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "UPDATING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
        "UPDATING",
    )
)


def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatus value: {data!r}")
    return cast(ApplicationStatus, data)
