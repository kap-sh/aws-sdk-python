"""Generated from Smithy shape ``com.amazonaws.devopsguru#LogAnomalyClasses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.log_anomaly_class

LogAnomalyClasses: TypeAlias = list[
    "aws_sdk_devops_guru.types.log_anomaly_class.LogAnomalyClass"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogAnomalyClasses) -> list:
    import aws_sdk_devops_guru.types.log_anomaly_class

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.log_anomaly_class.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogAnomalyClasses:
    import aws_sdk_devops_guru.types.log_anomaly_class

    out: LogAnomalyClasses = []
    for item in data:
        out.append(aws_sdk_devops_guru.types.log_anomaly_class.deserialize_json(item))
    return out
