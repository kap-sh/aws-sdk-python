"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonDeploymentAlarms``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status
    import aws_sdk_ecs.types.string_list


class DaemonDeploymentAlarms(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status.DaemonDeploymentRollbackMonitorsStatus"
    ]
    """<p>The status of the alarms check. Amazon ECS is not using alarms for daemon deployment failures when the status is <code>DISABLED</code>.</p>"""
    alarm_names: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The name of the CloudWatch alarms that determine when a daemon deployment failed.</p>"""
    triggered_alarm_names: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>One or more CloudWatch alarm names that have been triggered during the daemon deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonDeploymentAlarms) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status

        out["status"] = (
            aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "alarm_names" in value:
        import aws_sdk_ecs.types.string_list

        out["alarmNames"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["alarm_names"]
        )
    if "triggered_alarm_names" in value:
        import aws_sdk_ecs.types.string_list

        out["triggeredAlarmNames"] = (
            aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
                value["triggered_alarm_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonDeploymentAlarms:
    out: DaemonDeploymentAlarms = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status

        out["status"] = (
            aws_sdk_ecs.types.daemon_deployment_rollback_monitors_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "alarmNames" in data:
        import aws_sdk_ecs.types.string_list

        out["alarm_names"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["alarmNames"]
        )
    if "triggeredAlarmNames" in data:
        import aws_sdk_ecs.types.string_list

        out["triggered_alarm_names"] = (
            aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
                data["triggeredAlarmNames"]
            )
        )
    return out
