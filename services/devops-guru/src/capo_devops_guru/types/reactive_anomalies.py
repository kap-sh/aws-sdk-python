"""Generated from Smithy shape ``com.amazonaws.devopsguru#ReactiveAnomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.reactive_anomaly_summary

ReactiveAnomalies: TypeAlias = list[
    "capo_devops_guru.types.reactive_anomaly_summary.ReactiveAnomalySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReactiveAnomalies) -> list:
    import capo_devops_guru.types.reactive_anomaly_summary

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.reactive_anomaly_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReactiveAnomalies:
    import capo_devops_guru.types.reactive_anomaly_summary

    out: ReactiveAnomalies = []
    for item in data:
        out.append(
            capo_devops_guru.types.reactive_anomaly_summary.deserialize_json(item)
        )
    return out
