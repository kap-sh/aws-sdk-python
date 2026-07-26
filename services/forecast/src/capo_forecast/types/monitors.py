"""Generated from Smithy shape ``com.amazonaws.forecast#Monitors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.monitor_summary

Monitors: TypeAlias = list["capo_forecast.types.monitor_summary.MonitorSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Monitors) -> list:
    import capo_forecast.types.monitor_summary

    out: list = []
    for item in value:
        out.append(capo_forecast.types.monitor_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Monitors:
    import capo_forecast.types.monitor_summary

    out: Monitors = []
    for item in data:
        out.append(capo_forecast.types.monitor_summary.deserialize_aws_json_1_1(item))
    return out
