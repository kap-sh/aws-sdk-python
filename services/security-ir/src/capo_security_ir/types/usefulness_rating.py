"""Generated from Smithy shape ``com.amazonaws.securityir#UsefulnessRating``."""

from typing import Literal, TypeAlias, cast

UsefulnessRating: TypeAlias = Literal[
    "USEFUL",
    "NOT_USEFUL",
]


# --- restJson1 ser/de ---
def serialize_json(value: UsefulnessRating) -> str:
    return value


def deserialize_json(data: str) -> UsefulnessRating:
    return cast(UsefulnessRating, data)
