"""Generated from Smithy shape ``com.amazonaws.batch#JQStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

JQStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "DELETED",
    "VALID",
    "INVALID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "DELETING",
        "DELETED",
        "VALID",
        "INVALID",
    )
)


def serialize_json(value: JQStatus) -> str:
    return value


def deserialize_json(data: str) -> JQStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JQStatus value: {data!r}")
    return cast(JQStatus, data)
