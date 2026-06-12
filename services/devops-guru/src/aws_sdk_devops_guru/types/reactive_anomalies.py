"""Generated from Smithy shape ``com.amazonaws.devopsguru#ReactiveAnomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.reactive_anomaly_summary

ReactiveAnomalies: TypeAlias = list[
    "aws_sdk_devops_guru.types.reactive_anomaly_summary.ReactiveAnomalySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReactiveAnomalies) -> list:
    import aws_sdk_devops_guru.types.reactive_anomaly_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.reactive_anomaly_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReactiveAnomalies:
    import aws_sdk_devops_guru.types.reactive_anomaly_summary

    out: ReactiveAnomalies = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.reactive_anomaly_summary.deserialize_json(item)
        )
    return out
