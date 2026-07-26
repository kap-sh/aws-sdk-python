"""Generated from Smithy shape ``com.amazonaws.devopsguru#ProactiveAnomalies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.proactive_anomaly_summary

ProactiveAnomalies: TypeAlias = list[
    "capo_devops_guru.types.proactive_anomaly_summary.ProactiveAnomalySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveAnomalies) -> list:
    import capo_devops_guru.types.proactive_anomaly_summary

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.proactive_anomaly_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProactiveAnomalies:
    import capo_devops_guru.types.proactive_anomaly_summary

    out: ProactiveAnomalies = []
    for item in data:
        out.append(
            capo_devops_guru.types.proactive_anomaly_summary.deserialize_json(item)
        )
    return out
