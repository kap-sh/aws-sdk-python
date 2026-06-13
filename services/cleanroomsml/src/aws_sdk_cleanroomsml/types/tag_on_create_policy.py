"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TagOnCreatePolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

TagOnCreatePolicy: TypeAlias = Literal[
    "FROM_PARENT_RESOURCE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FROM_PARENT_RESOURCE",
        "NONE",
    )
)


def serialize_json(value: TagOnCreatePolicy) -> str:
    return value


def deserialize_json(data: str) -> TagOnCreatePolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TagOnCreatePolicy value: {data!r}")
    return cast(TagOnCreatePolicy, data)
