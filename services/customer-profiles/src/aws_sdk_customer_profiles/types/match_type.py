"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchType``."""

from typing import Literal, TypeAlias, cast

MatchType: TypeAlias = Literal[
    "RULE_BASED_MATCHING",
    "ML_BASED_MATCHING",
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchType) -> str:
    return value


def deserialize_json(data: str) -> MatchType:
    return cast(MatchType, data)
