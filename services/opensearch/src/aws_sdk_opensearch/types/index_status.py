"""Generated from Smithy shape ``com.amazonaws.opensearch#IndexStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

IndexStatus: TypeAlias = Literal[
    "CREATED",
    "UPDATED",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATED",
        "UPDATED",
        "DELETED",
    )
)


def serialize_json(value: IndexStatus) -> str:
    return value


def deserialize_json(data: str) -> IndexStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IndexStatus value: {data!r}")
    return cast(IndexStatus, data)
