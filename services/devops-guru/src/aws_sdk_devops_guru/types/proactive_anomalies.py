"""Generated from Smithy shape ``com.amazonaws.devopsguru#ProactiveAnomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.proactive_anomaly_summary

ProactiveAnomalies: TypeAlias = list[
    "aws_sdk_devops_guru.types.proactive_anomaly_summary.ProactiveAnomalySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveAnomalies) -> list:
    import aws_sdk_devops_guru.types.proactive_anomaly_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.proactive_anomaly_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProactiveAnomalies:
    import aws_sdk_devops_guru.types.proactive_anomaly_summary

    out: ProactiveAnomalies = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.proactive_anomaly_summary.deserialize_json(item)
        )
    return out
