"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentAlarms``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status
    import aws_sdk_ecs.types.string_list


class DaemonDeploymentAlarms(TypedDict):
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status.DaemonDeploymentRollbackMonitorsStatus"
    ]
    """<p>The status of the alarms check. Amazon ECS is not using alarms for daemon deployment failures when the status is <code>DISABLED</code>.</p>"""
    alarm_names: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The name of the CloudWatch alarms that determine when a daemon deployment failed.</p>"""
    triggered_alarm_names: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>One or more CloudWatch alarm names that have been triggered during the daemon deployment.</p>"""
