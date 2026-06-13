"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregationSortConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_sort_configuration

AggregationSortConfigurationList: TypeAlias = list[
    "aws_sdk_quicksight.types.aggregation_sort_configuration.AggregationSortConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AggregationSortConfigurationList) -> list:
    import aws_sdk_quicksight.types.aggregation_sort_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.aggregation_sort_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AggregationSortConfigurationList:
    import aws_sdk_quicksight.types.aggregation_sort_configuration

    out: AggregationSortConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.aggregation_sort_configuration.deserialize_json(
                item
            )
        )
    return out
