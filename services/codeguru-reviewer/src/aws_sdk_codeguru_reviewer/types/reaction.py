"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Reaction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

Reaction: TypeAlias = Literal[
    "ThumbsUp",
    "ThumbsDown",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ThumbsUp",
        "ThumbsDown",
    )
)


def serialize_json(value: Reaction) -> str:
    return value


def deserialize_json(data: str) -> Reaction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Reaction value: {data!r}")
    return cast(Reaction, data)
