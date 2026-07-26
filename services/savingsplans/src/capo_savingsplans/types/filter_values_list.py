"""Generated from Smithy shape ``com.amazonaws.savingsplans#FilterValuesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.json_safe_filter_value_string

FilterValuesList: TypeAlias = list[
    "capo_savingsplans.types.json_safe_filter_value_string.JsonSafeFilterValueString"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterValuesList) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterValuesList:
    return list(data)
