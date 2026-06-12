"""Generated from Smithy shape ``com.amazonaws.artifact#PublishedState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_artifact.errors import DeserializationError

PublishedState: TypeAlias = Literal[
    "PUBLISHED",
    "UNPUBLISHED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISHED",
        "UNPUBLISHED",
    )
)


def serialize_json(value: PublishedState) -> str:
    return value


def deserialize_json(data: str) -> PublishedState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PublishedState value: {data!r}")
    return cast(PublishedState, data)
