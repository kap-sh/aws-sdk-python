"""Generated from Smithy shape ``com.amazonaws.pipes#IncludeExecutionData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.include_execution_data_option

IncludeExecutionData: TypeAlias = list[
    "capo_pipes.types.include_execution_data_option.IncludeExecutionDataOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncludeExecutionData) -> list:
    return list(value)


def deserialize_json(data: list) -> IncludeExecutionData:
    return list(data)
