"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedMetricAlarms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.managed_metric_alarm

ManagedMetricAlarms: TypeAlias = list[
    "capo_ecs.types.managed_metric_alarm.ManagedMetricAlarm"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedMetricAlarms) -> list:
    import capo_ecs.types.managed_metric_alarm

    out: list = []
    for item in value:
        out.append(capo_ecs.types.managed_metric_alarm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ManagedMetricAlarms:
    import capo_ecs.types.managed_metric_alarm

    out: ManagedMetricAlarms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.managed_metric_alarm.deserialize_aws_json_1_1(item))
    return out
