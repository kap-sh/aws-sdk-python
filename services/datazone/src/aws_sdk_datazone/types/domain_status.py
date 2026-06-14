"""Generated from Smithy shape ``com.amazonaws.datazone#DomainStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DomainStatus: TypeAlias = Literal[
    "CREATING",
    "AVAILABLE",
    "CREATION_FAILED",
    "DELETING",
    "DELETED",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "AVAILABLE",
        "CREATION_FAILED",
        "DELETING",
        "DELETED",
        "DELETION_FAILED",
    )
)


def serialize_json(value: DomainStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainStatus value: {data!r}")
    return cast(DomainStatus, data)
