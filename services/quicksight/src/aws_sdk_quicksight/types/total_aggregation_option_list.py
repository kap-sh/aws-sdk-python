"""Generated from Smithy shape ``com.amazonaws.quicksight#TotalAggregationOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.total_aggregation_option

TotalAggregationOptionList: TypeAlias = list[
    "aws_sdk_quicksight.types.total_aggregation_option.TotalAggregationOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: TotalAggregationOptionList) -> list:
    import aws_sdk_quicksight.types.total_aggregation_option

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.total_aggregation_option.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TotalAggregationOptionList:
    import aws_sdk_quicksight.types.total_aggregation_option

    out: TotalAggregationOptionList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.total_aggregation_option.deserialize_json(item)
        )
    return out
