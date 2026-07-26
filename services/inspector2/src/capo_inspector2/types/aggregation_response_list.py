"""Generated from Smithy shape ``com.amazonaws.inspector2#AggregationResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.aggregation_response

AggregationResponseList: TypeAlias = list[
    "capo_inspector2.types.aggregation_response.AggregationResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationResponseList) -> list:
    import capo_inspector2.types.aggregation_response

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.aggregation_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationResponseList:
    import capo_inspector2.types.aggregation_response

    out: AggregationResponseList = []
    for item in data:
        out.append(capo_inspector2.types.aggregation_response.deserialize_json(item))
    return out
