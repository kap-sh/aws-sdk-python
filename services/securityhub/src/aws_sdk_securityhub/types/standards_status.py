"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

StandardsStatus: TypeAlias = Literal[
    "PENDING",
    "READY",
    "FAILED",
    "DELETING",
    "INCOMPLETE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "READY",
        "FAILED",
        "DELETING",
        "INCOMPLETE",
    )
)


def serialize_json(value: StandardsStatus) -> str:
    return value


def deserialize_json(data: str) -> StandardsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StandardsStatus value: {data!r}")
    return cast(StandardsStatus, data)
