"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetricSortCriteriaMaxOne``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.current_metric_sort_criteria

CurrentMetricSortCriteriaMaxOne: TypeAlias = list[
    "aws_sdk_connect.types.current_metric_sort_criteria.CurrentMetricSortCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetricSortCriteriaMaxOne) -> list:
    import aws_sdk_connect.types.current_metric_sort_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.current_metric_sort_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CurrentMetricSortCriteriaMaxOne:
    import aws_sdk_connect.types.current_metric_sort_criteria

    out: CurrentMetricSortCriteriaMaxOne = []
    for item in data:
        out.append(
            aws_sdk_connect.types.current_metric_sort_criteria.deserialize_json(item)
        )
    return out
