"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.filter_operation

FilterOperationList: TypeAlias = list[
    "aws_sdk_quicksight.types.filter_operation.FilterOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperationList) -> list:
    import aws_sdk_quicksight.types.filter_operation

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.filter_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterOperationList:
    import aws_sdk_quicksight.types.filter_operation

    out: FilterOperationList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.filter_operation.deserialize_json(item))
    return out
