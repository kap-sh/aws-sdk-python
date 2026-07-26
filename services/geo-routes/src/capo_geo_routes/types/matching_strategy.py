"""Generated from Smithy shape ``com.amazonaws.georoutes#MatchingStrategy``."""

from typing import Literal, TypeAlias, cast

MatchingStrategy: TypeAlias = Literal[
    "MatchAny",
    "MatchMostSignificantRoad",
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchingStrategy) -> str:
    return value


def deserialize_json(data: str) -> MatchingStrategy:
    return cast(MatchingStrategy, data)
