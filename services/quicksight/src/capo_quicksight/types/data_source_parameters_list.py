"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.data_source_parameters

DataSourceParametersList: TypeAlias = list[
    "capo_quicksight.types.data_source_parameters.DataSourceParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceParametersList) -> list:
    import capo_quicksight.types.data_source_parameters

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.data_source_parameters.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceParametersList:
    import capo_quicksight.types.data_source_parameters

    out: DataSourceParametersList = []
    for item in data:
        out.append(capo_quicksight.types.data_source_parameters.deserialize_json(item))
    return out
