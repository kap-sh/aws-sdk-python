"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_alarm_configuration
    import aws_sdk_ecs.types.daemon_drain_percent
    import aws_sdk_ecs.types.integer


class DaemonDeploymentConfiguration(TypedDict):
    drain_percent: NotRequired[
        "aws_sdk_ecs.types.daemon_drain_percent.DaemonDrainPercent"
    ]
    """<p>The percentage of container instances to drain simultaneously during a daemon deployment. Valid values are between 0.0 and 100.0.</p>"""
    alarms: NotRequired[
        "aws_sdk_ecs.types.daemon_alarm_configuration.DaemonAlarmConfiguration"
    ]
    """<p>The CloudWatch alarm configuration for the daemon deployment. When alarms are triggered during a deployment, the deployment can be automatically rolled back.</p>"""
    bake_time_in_minutes: "aws_sdk_ecs.types.integer.Integer"
    """<p>The amount of time (in minutes) to wait after a successful deployment step before proceeding. This allows time to monitor for issues before continuing. The default value is 0.</p>"""
