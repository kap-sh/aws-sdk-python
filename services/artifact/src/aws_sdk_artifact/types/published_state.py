"""Generated from Smithy shape ``com.amazonaws.artifact#PublishedState``."""

from typing import Literal, TypeAlias, cast

PublishedState: TypeAlias = Literal[
    "PUBLISHED",
    "UNPUBLISHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PublishedState) -> str:
    return value


def deserialize_json(data: str) -> PublishedState:
    return cast(PublishedState, data)
