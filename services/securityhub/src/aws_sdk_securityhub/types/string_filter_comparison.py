"""Generated from Smithy shape ``com.amazonaws.securityhub#StringFilterComparison``."""

from typing import Literal, TypeAlias, cast

StringFilterComparison: TypeAlias = Literal[
    "EQUALS",
    "PREFIX",
    "NOT_EQUALS",
    "PREFIX_NOT_EQUALS",
    "CONTAINS",
    "NOT_CONTAINS",
    "CONTAINS_WORD",
]


# --- restJson1 ser/de ---
def serialize_json(value: StringFilterComparison) -> str:
    return value


def deserialize_json(data: str) -> StringFilterComparison:
    return cast(StringFilterComparison, data)
