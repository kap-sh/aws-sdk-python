"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedMetricAlarms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_metric_alarm

ManagedMetricAlarms: TypeAlias = list[
    "aws_sdk_ecs.types.managed_metric_alarm.ManagedMetricAlarm"
]
