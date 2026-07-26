"""Generated from Smithy shape ``com.amazonaws.devopsguru#TimestampMetricValuePairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.timestamp_metric_value_pair

TimestampMetricValuePairList: TypeAlias = list[
    "capo_devops_guru.types.timestamp_metric_value_pair.TimestampMetricValuePair"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimestampMetricValuePairList) -> list:
    import capo_devops_guru.types.timestamp_metric_value_pair

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.timestamp_metric_value_pair.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TimestampMetricValuePairList:
    import capo_devops_guru.types.timestamp_metric_value_pair

    out: TimestampMetricValuePairList = []
    for item in data:
        out.append(
            capo_devops_guru.types.timestamp_metric_value_pair.deserialize_json(item)
        )
    return out
