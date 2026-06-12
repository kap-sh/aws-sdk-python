"""Generated from Smithy shape ``com.amazonaws.datazone#AggregationOutputList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.aggregation_output

AggregationOutputList: TypeAlias = list["aws_sdk_datazone.types.aggregation_output.AggregationOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationOutputList) -> list:
    import aws_sdk_datazone.types.aggregation_output
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.aggregation_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationOutputList:
    import aws_sdk_datazone.types.aggregation_output
    out: AggregationOutputList = []
    for item in data:
        out.append(aws_sdk_datazone.types.aggregation_output.deserialize_json(item))
    return out