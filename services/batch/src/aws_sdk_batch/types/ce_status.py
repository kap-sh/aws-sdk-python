"""Generated from Smithy shape ``com.amazonaws.batch#CEStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

CEStatus: TypeAlias = Literal[
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


def serialize_json(value: CEStatus) -> str:
    return value


def deserialize_json(data: str) -> CEStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CEStatus value: {data!r}")
    return cast(CEStatus, data)
