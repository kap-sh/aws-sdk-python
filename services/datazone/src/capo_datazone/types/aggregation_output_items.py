"""Generated from Smithy shape ``com.amazonaws.datazone#AggregationOutputItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.aggregation_output_item

AggregationOutputItems: TypeAlias = list[
    "capo_datazone.types.aggregation_output_item.AggregationOutputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationOutputItems) -> list:
    import capo_datazone.types.aggregation_output_item

    out: list = []
    for item in value:
        out.append(capo_datazone.types.aggregation_output_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationOutputItems:
    import capo_datazone.types.aggregation_output_item

    out: AggregationOutputItems = []
    for item in data:
        out.append(capo_datazone.types.aggregation_output_item.deserialize_json(item))
    return out
