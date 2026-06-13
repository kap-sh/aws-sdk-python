"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchPurpose``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_entityresolution.errors import DeserializationError

MatchPurpose: TypeAlias = Literal[
    "IDENTIFIER_GENERATION",
    "INDEXING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDENTIFIER_GENERATION",
        "INDEXING",
    )
)


def serialize_json(value: MatchPurpose) -> str:
    return value


def deserialize_json(data: str) -> MatchPurpose:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MatchPurpose value: {data!r}")
    return cast(MatchPurpose, data)
