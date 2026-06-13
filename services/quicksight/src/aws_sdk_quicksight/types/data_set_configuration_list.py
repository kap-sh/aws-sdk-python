"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_configuration

DataSetConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_set_configuration.DataSetConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetConfigurationList) -> list:
    import aws_sdk_quicksight.types.data_set_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.data_set_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> DataSetConfigurationList:
    import aws_sdk_quicksight.types.data_set_configuration

    out: DataSetConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.data_set_configuration.deserialize_json(item)
        )
    return out
