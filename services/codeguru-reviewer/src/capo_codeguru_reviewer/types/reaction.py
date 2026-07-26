"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Reaction``."""

from typing import Literal, TypeAlias, cast

Reaction: TypeAlias = Literal[
    "ThumbsUp",
    "ThumbsDown",
]


# --- restJson1 ser/de ---
def serialize_json(value: Reaction) -> str:
    return value


def deserialize_json(data: str) -> Reaction:
    return cast(Reaction, data)
