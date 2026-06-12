"""Generated from Smithy shape ``com.amazonaws.georoutes#MatchingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

MatchingStrategy: TypeAlias = Literal[
    "MatchAny",
    "MatchMostSignificantRoad",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MatchAny",
        "MatchMostSignificantRoad",
    )
)


def serialize_json(value: MatchingStrategy) -> str:
    return value


def deserialize_json(data: str) -> MatchingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MatchingStrategy value: {data!r}")
    return cast(MatchingStrategy, data)
