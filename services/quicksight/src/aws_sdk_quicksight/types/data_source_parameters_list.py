"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSourceParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_source_parameters

DataSourceParametersList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_source_parameters.DataSourceParameters"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceParametersList) -> list:
    import aws_sdk_quicksight.types.data_source_parameters

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.data_source_parameters.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSourceParametersList:
    import aws_sdk_quicksight.types.data_source_parameters

    out: DataSourceParametersList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.data_source_parameters.deserialize_json(item)
        )
    return out
