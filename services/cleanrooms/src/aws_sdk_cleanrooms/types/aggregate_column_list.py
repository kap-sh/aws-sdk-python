"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AggregateColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.aggregate_column

AggregateColumnList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.aggregate_column.AggregateColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregateColumnList) -> list:
    import aws_sdk_cleanrooms.types.aggregate_column

    out: list = []
    for item in value:
        out.append(aws_sdk_cleanrooms.types.aggregate_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregateColumnList:
    import aws_sdk_cleanrooms.types.aggregate_column

    out: AggregateColumnList = []
    for item in data:
        out.append(aws_sdk_cleanrooms.types.aggregate_column.deserialize_json(item))
    return out
