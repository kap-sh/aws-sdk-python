"""Generated from Smithy shape ``com.amazonaws.devopsguru#CloudWatchMetricsDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.cloud_watch_metrics_detail

CloudWatchMetricsDetails: TypeAlias = list[
    "aws_sdk_devops_guru.types.cloud_watch_metrics_detail.CloudWatchMetricsDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMetricsDetails) -> list:
    import aws_sdk_devops_guru.types.cloud_watch_metrics_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.cloud_watch_metrics_detail.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CloudWatchMetricsDetails:
    import aws_sdk_devops_guru.types.cloud_watch_metrics_detail

    out: CloudWatchMetricsDetails = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.cloud_watch_metrics_detail.deserialize_json(item)
        )
    return out
