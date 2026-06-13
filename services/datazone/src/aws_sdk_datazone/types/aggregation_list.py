"""Generated from Smithy shape ``com.amazonaws.datazone#AggregationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aggregation_list_item

AggregationList: TypeAlias = list[
    "aws_sdk_datazone.types.aggregation_list_item.AggregationListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationList) -> list:
    import aws_sdk_datazone.types.aggregation_list_item

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.aggregation_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationList:
    import aws_sdk_datazone.types.aggregation_list_item

    out: AggregationList = []
    for item in data:
        out.append(aws_sdk_datazone.types.aggregation_list_item.deserialize_json(item))
    return out
