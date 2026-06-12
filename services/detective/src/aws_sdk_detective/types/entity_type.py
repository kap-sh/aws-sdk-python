"""Generated from Smithy shape ``com.amazonaws.detective#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_detective.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "IAM_ROLE",
    "IAM_USER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IAM_ROLE",
        "IAM_USER",
    )
)


def serialize_json(value: EntityType) -> str:
    return value


def deserialize_json(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
