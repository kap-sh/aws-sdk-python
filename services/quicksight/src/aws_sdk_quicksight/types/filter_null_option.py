"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterNullOption``."""

from typing import Literal, TypeAlias, cast

FilterNullOption: TypeAlias = Literal[
    "ALL_VALUES",
    "NULLS_ONLY",
    "NON_NULLS_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterNullOption) -> str:
    return value


def deserialize_json(data: str) -> FilterNullOption:
    return cast(FilterNullOption, data)
