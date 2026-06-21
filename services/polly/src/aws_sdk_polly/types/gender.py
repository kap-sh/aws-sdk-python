"""Generated from Smithy shape ``com.amazonaws.polly#Gender``."""

from typing import Literal, TypeAlias, cast

Gender: TypeAlias = Literal[
    "Female",
    "Male",
]


# --- restJson1 ser/de ---
def serialize_json(value: Gender) -> str:
    return value


def deserialize_json(data: str) -> Gender:
    return cast(Gender, data)
