"""Generated from Smithy shape ``com.amazonaws.quicksight#NullFilterOption``."""

from typing import Literal, TypeAlias, cast

NullFilterOption: TypeAlias = Literal[
    "ALL_VALUES",
    "NON_NULLS_ONLY",
    "NULLS_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: NullFilterOption) -> str:
    return value


def deserialize_json(data: str) -> NullFilterOption:
    return cast(NullFilterOption, data)
