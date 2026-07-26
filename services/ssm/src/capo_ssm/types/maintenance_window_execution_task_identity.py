"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowExecutionTaskIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.alarm_state_information_list
    import capo_ssm.types.date_time
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_status
    import capo_ssm.types.maintenance_window_execution_status_details
    import capo_ssm.types.maintenance_window_execution_task_id
    import capo_ssm.types.maintenance_window_task_arn
    import capo_ssm.types.maintenance_window_task_type


class MaintenanceWindowExecutionTaskIdentity(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The ID of the maintenance window execution that ran the task.</p>"""
    task_execution_id: NotRequired[
        "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    ]
    """<p>The ID of the specific task execution in the maintenance window execution.</p>"""
    status: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status.MaintenanceWindowExecutionStatus"
    ]
    """<p>The status of the task execution.</p>"""
    status_details: NotRequired[
        "capo_ssm.types.maintenance_window_execution_status_details.MaintenanceWindowExecutionStatusDetails"
    ]
    """<p>The details explaining the status of the task execution. Not available for all status values.</p>"""
    start_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the task execution started.</p>"""
    end_time: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The time the task execution finished.</p>"""
    task_arn: NotRequired[
        "capo_ssm.types.maintenance_window_task_arn.MaintenanceWindowTaskArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the task that ran.</p>"""
    task_type: NotRequired[
        "capo_ssm.types.maintenance_window_task_type.MaintenanceWindowTaskType"
    ]
    """<p>The type of task that ran.</p>"""
    alarm_configuration: NotRequired[
        "capo_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm applied to your maintenance window task.</p>"""
    triggered_alarms: NotRequired[
        "capo_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarm that was invoked by the maintenance window task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowExecutionTaskIdentity) -> dict:
    out: dict = {}
    if "window_execution_id" in value:
        out["WindowExecutionId"] = value["window_execution_id"]
    if "task_execution_id" in value:
        out["TaskExecutionId"] = value["task_execution_id"]
    if "status" in value:
        import capo_ssm.types.maintenance_window_execution_status

        out["Status"] = (
            capo_ssm.types.maintenance_window_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "start_time" in value:
        import capo_ssm.types.date_time

        out["StartTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_ssm.types.date_time

        out["EndTime"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "task_type" in value:
        import capo_ssm.types.maintenance_window_task_type

        out["TaskType"] = (
            capo_ssm.types.maintenance_window_task_type.serialize_aws_json_1_1(
                value["task_type"]
            )
        )
    if "alarm_configuration" in value:
        import capo_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            capo_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "triggered_alarms" in value:
        import capo_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            capo_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MaintenanceWindowExecutionTaskIdentity:
    out: MaintenanceWindowExecutionTaskIdentity = {}  # type: ignore[typeddict-item]
    if "WindowExecutionId" in data:
        out["window_execution_id"] = data["WindowExecutionId"]
    if "TaskExecutionId" in data:
        out["task_execution_id"] = data["TaskExecutionId"]
    if "Status" in data:
        import capo_ssm.types.maintenance_window_execution_status

        out["status"] = (
            capo_ssm.types.maintenance_window_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusDetails" in data:
        out["status_details"] = data["StatusDetails"]
    if "StartTime" in data:
        import capo_ssm.types.date_time

        out["start_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import capo_ssm.types.date_time

        out["end_time"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "TaskType" in data:
        import capo_ssm.types.maintenance_window_task_type

        out["task_type"] = (
            capo_ssm.types.maintenance_window_task_type.deserialize_aws_json_1_1(
                data["TaskType"]
            )
        )
    if "AlarmConfiguration" in data:
        import capo_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            capo_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if "TriggeredAlarms" in data:
        import capo_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            capo_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    return out
