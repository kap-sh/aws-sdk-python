"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchPurpose``."""

from typing import Literal, TypeAlias, cast

MatchPurpose: TypeAlias = Literal[
    "IDENTIFIER_GENERATION",
    "INDEXING",
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchPurpose) -> str:
    return value


def deserialize_json(data: str) -> MatchPurpose:
    return cast(MatchPurpose, data)
