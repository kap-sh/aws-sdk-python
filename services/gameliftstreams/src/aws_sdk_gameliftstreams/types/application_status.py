"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gameliftstreams.errors import DeserializationError

ApplicationStatus: TypeAlias = Literal[
    "INITIALIZED",
    "PROCESSING",
    "READY",
    "DELETING",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZED",
        "PROCESSING",
        "READY",
        "DELETING",
        "ERROR",
    )
)


def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationStatus value: {data!r}")
    return cast(ApplicationStatus, data)
