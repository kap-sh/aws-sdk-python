"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_configuration

ColumnConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.column_configuration.ColumnConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnConfigurationList) -> list:
    import aws_sdk_quicksight.types.column_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.column_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnConfigurationList:
    import aws_sdk_quicksight.types.column_configuration

    out: ColumnConfigurationList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.column_configuration.deserialize_json(item))
    return out
