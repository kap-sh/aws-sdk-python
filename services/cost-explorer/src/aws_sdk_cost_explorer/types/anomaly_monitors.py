"""Generated from Smithy shape ``com.amazonaws.costexplorer#AnomalyMonitors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.anomaly_monitor

AnomalyMonitors: TypeAlias = list[
    "aws_sdk_cost_explorer.types.anomaly_monitor.AnomalyMonitor"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnomalyMonitors) -> list:
    import aws_sdk_cost_explorer.types.anomaly_monitor

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.anomaly_monitor.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AnomalyMonitors:
    import aws_sdk_cost_explorer.types.anomaly_monitor

    out: AnomalyMonitors = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.anomaly_monitor.deserialize_aws_json_1_1(item)
        )
    return out
