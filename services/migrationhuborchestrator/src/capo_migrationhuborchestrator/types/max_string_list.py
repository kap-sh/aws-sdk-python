"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#MaxStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.max_string_value

MaxStringList: TypeAlias = list[
    "capo_migrationhuborchestrator.types.max_string_value.MaxStringValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: MaxStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> MaxStringList:
    return list(data)
