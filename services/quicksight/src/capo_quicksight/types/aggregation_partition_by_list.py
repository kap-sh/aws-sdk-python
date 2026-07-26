"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregationPartitionByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.aggregation_partition_by

AggregationPartitionByList: TypeAlias = list[
    "capo_quicksight.types.aggregation_partition_by.AggregationPartitionBy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationPartitionByList) -> list:
    import capo_quicksight.types.aggregation_partition_by

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.aggregation_partition_by.serialize_json(item))
    return out


def deserialize_json(data: list) -> AggregationPartitionByList:
    import capo_quicksight.types.aggregation_partition_by

    out: AggregationPartitionByList = []
    for item in data:
        out.append(
            capo_quicksight.types.aggregation_partition_by.deserialize_json(item)
        )
    return out
