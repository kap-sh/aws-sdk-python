"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricsDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.cloud_watch_metrics_dimension

CloudWatchMetricsDimensions: TypeAlias = list[
    "capo_devops_guru.types.cloud_watch_metrics_dimension.CloudWatchMetricsDimension"
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMetricsDimensions) -> list:
    import capo_devops_guru.types.cloud_watch_metrics_dimension

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.cloud_watch_metrics_dimension.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CloudWatchMetricsDimensions:
    import capo_devops_guru.types.cloud_watch_metrics_dimension

    out: CloudWatchMetricsDimensions = []
    for item in data:
        out.append(
            capo_devops_guru.types.cloud_watch_metrics_dimension.deserialize_json(item)
        )
    return out
