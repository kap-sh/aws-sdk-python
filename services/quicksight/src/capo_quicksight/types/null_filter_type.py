"""Generated from Smithy shape ``com.amazonaws.quicksight#NullFilterType``."""

from typing import Literal, TypeAlias, cast

NullFilterType: TypeAlias = Literal[
    "ALL_VALUES",
    "NON_NULLS_ONLY",
    "NULLS_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: NullFilterType) -> str:
    return value


def deserialize_json(data: str) -> NullFilterType:
    return cast(NullFilterType, data)
