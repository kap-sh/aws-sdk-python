"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.column_configuration

ColumnConfigurationList: TypeAlias = list[
    "capo_quicksight.types.column_configuration.ColumnConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnConfigurationList) -> list:
    import capo_quicksight.types.column_configuration

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.column_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnConfigurationList:
    import capo_quicksight.types.column_configuration

    out: ColumnConfigurationList = []
    for item in data:
        out.append(capo_quicksight.types.column_configuration.deserialize_json(item))
    return out
