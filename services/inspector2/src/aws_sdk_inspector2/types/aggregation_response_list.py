"""Generated from Smithy shape ``com.amazonaws.inspector2#AggregationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_inspector2.types.aggregation_response

AggregationResponseList: TypeAlias = list["aws_sdk_inspector2.types.aggregation_response.AggregationResponse"]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationResponseList) -> list:
    import aws_sdk_inspector2.types.aggregation_response
    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.aggregation_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationResponseList:
    import aws_sdk_inspector2.types.aggregation_response
    out: AggregationResponseList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.aggregation_response.deserialize_json(item))
    return out