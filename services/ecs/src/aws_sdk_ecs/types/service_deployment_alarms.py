"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceDeploymentAlarms``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_deployment_rollback_monitors_status
    import aws_sdk_ecs.types.string_list


class ServiceDeploymentAlarms(TypedDict):
    status: NotRequired[
        "aws_sdk_ecs.types.service_deployment_rollback_monitors_status.ServiceDeploymentRollbackMonitorsStatus"
    ]
    """<p>The status of the alarms check. Amazon ECS is not using alarms for service deployment failures when the status is <code>DISABLED</code>.</p>"""
    alarm_names: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The name of the CloudWatch alarms that determine when a service deployment failed. A \",\" separates the alarms.</p>"""
    triggered_alarm_names: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>One or more CloudWatch alarm names that have been triggered during the service deployment. A \",\" separates the alarm names.</p>"""
