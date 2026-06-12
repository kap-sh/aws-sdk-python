"""Generated from Smithy shape ``com.amazonaws.devopsguru#LogAnomalyShowcases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.log_anomaly_showcase

LogAnomalyShowcases: TypeAlias = list[
    "aws_sdk_devops_guru.types.log_anomaly_showcase.LogAnomalyShowcase"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogAnomalyShowcases) -> list:
    import aws_sdk_devops_guru.types.log_anomaly_showcase

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.log_anomaly_showcase.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogAnomalyShowcases:
    import aws_sdk_devops_guru.types.log_anomaly_showcase

    out: LogAnomalyShowcases = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.log_anomaly_showcase.deserialize_json(item)
        )
    return out
