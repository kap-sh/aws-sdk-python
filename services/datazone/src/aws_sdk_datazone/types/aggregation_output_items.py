"""Generated from Smithy shape ``com.amazonaws.datazone#AggregationOutputItems``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.aggregation_output_item

AggregationOutputItems: TypeAlias = list["aws_sdk_datazone.types.aggregation_output_item.AggregationOutputItem"]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationOutputItems) -> list:
    import aws_sdk_datazone.types.aggregation_output_item
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.aggregation_output_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationOutputItems:
    import aws_sdk_datazone.types.aggregation_output_item
    out: AggregationOutputItems = []
    for item in data:
        out.append(aws_sdk_datazone.types.aggregation_output_item.deserialize_json(item))
    return out