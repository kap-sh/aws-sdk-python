"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation

AggregationList: TypeAlias = list["aws_sdk_quicksight.types.aggregation.Aggregation"]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationList) -> list:
    import aws_sdk_quicksight.types.aggregation

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.aggregation.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationList:
    import aws_sdk_quicksight.types.aggregation

    out: AggregationList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.aggregation.deserialize_json(item))
    return out
