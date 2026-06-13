"""Generated from Smithy shape ``com.amazonaws.quicksight#TableUnaggregatedFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.unaggregated_field

TableUnaggregatedFieldList: TypeAlias = list[
    "aws_sdk_quicksight.types.unaggregated_field.UnaggregatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableUnaggregatedFieldList) -> list:
    import aws_sdk_quicksight.types.unaggregated_field

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.unaggregated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableUnaggregatedFieldList:
    import aws_sdk_quicksight.types.unaggregated_field

    out: TableUnaggregatedFieldList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.unaggregated_field.deserialize_json(item))
    return out
