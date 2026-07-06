"""Generated from Smithy shape ``com.amazonaws.ssm#GetMaintenanceWindowExecutionTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm_configuration
    import aws_sdk_ssm.types.alarm_state_information_list
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.maintenance_window_execution_id
    import aws_sdk_ssm.types.maintenance_window_execution_status
    import aws_sdk_ssm.types.maintenance_window_execution_status_details
    import aws_sdk_ssm.types.maintenance_window_execution_task_id
    import aws_sdk_ssm.types.maintenance_window_task_arn
    import aws_sdk_ssm.types.maintenance_window_task_parameters_list
    import aws_sdk_ssm.types.maintenance_window_task_priority
    import aws_sdk_ssm.types.maintenance_window_task_type
    import aws_sdk_ssm.types.max_concurrency
    import aws_sdk_ssm.types.max_errors
    import aws_sdk_ssm.types.service_role


class GetMaintenanceWindowExecutionTaskResult(TypedDict, closed=True):
    window_execution_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    ]
    """<p>The ID of the maintenance window execution that includes the task.</p>"""
    task_execution_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId"
    ]
    """<p>The ID of the specific task execution in the maintenance window task that was retrieved.</p>"""
    task_arn: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_arn.MaintenanceWindowTaskArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the task that ran.</p>"""
    service_role: NotRequired["aws_sdk_ssm.types.service_role.ServiceRole"]
    """<p>The role that was assumed when running the task.</p>"""
    type: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_type.MaintenanceWindowTaskType"
    ]
    """<p>The type of task that was run.</p>"""
    task_parameters: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_parameters_list.MaintenanceWindowTaskParametersList"
    ]
    """<p>The parameters passed to the task when it was run.</p> <note> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note> <p>The map has the following format:</p> <ul> <li> <p> <code>Key</code>: string, between 1 and 255 characters</p> </li> <li> <p> <code>Value</code>: an array of strings, each between 1 and 255 characters</p> </li> </ul>"""
    priority: "aws_sdk_ssm.types.maintenance_window_task_priority.MaintenanceWindowTaskPriority"
    """<p>The priority of the task.</p>"""
    max_concurrency: NotRequired["aws_sdk_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The defined maximum number of task executions that could be run in parallel.</p>"""
    max_errors: NotRequired["aws_sdk_ssm.types.max_errors.MaxErrors"]
    """<p>The defined maximum number of task execution errors allowed before scheduling of the task execution would have been stopped.</p>"""
    status: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_status.MaintenanceWindowExecutionStatus"
    ]
    """<p>The status of the task.</p>"""
    status_details: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_execution_status_details.MaintenanceWindowExecutionStatusDetails"
    ]
    """<p>The details explaining the status. Not available for all status values.</p>"""
    start_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the task execution started.</p>"""
    end_time: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The time the task execution completed.</p>"""
    alarm_configuration: NotRequired[
        "aws_sdk_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm you applied to your maintenance window task.</p>"""
    triggered_alarms: NotRequired[
        "aws_sdk_ssm.types.alarm_state_information_list.AlarmStateInformationList"
    ]
    """<p>The CloudWatch alarms that were invoked by the maintenance window task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaintenanceWindowExecutionTaskResult) -> dict:
    out: dict = {}
    if "window_execution_id" in value:
        out["WindowExecutionId"] = value["window_execution_id"]
    if "task_execution_id" in value:
        out["TaskExecutionId"] = value["task_execution_id"]
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "type" in value:
        import aws_sdk_ssm.types.maintenance_window_task_type

        out["Type"] = (
            aws_sdk_ssm.types.maintenance_window_task_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "task_parameters" in value:
        import aws_sdk_ssm.types.maintenance_window_task_parameters_list

        out["TaskParameters"] = (
            aws_sdk_ssm.types.maintenance_window_task_parameters_list.serialize_aws_json_1_1(
                value["task_parameters"]
            )
        )
    out["Priority"] = value.get("priority", 0)
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "status" in value:
        import aws_sdk_ssm.types.maintenance_window_execution_status

        out["Status"] = (
            aws_sdk_ssm.types.maintenance_window_execution_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "start_time" in value:
        import aws_sdk_ssm.types.date_time

        out["StartTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ssm.types.date_time

        out["EndTime"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "alarm_configuration" in value:
        import aws_sdk_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            aws_sdk_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    if "triggered_alarms" in value:
        import aws_sdk_ssm.types.alarm_state_information_list

        out["TriggeredAlarms"] = (
            aws_sdk_ssm.types.alarm_state_information_list.serialize_aws_json_1_1(
                value["triggered_alarms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaintenanceWindowExecutionTaskResult:
    out: GetMaintenanceWindowExecutionTaskResult = {}  # type: ignore[typeddict-item]
    if "WindowExecutionId" in data:
        out["window_execution_id"] = data["WindowExecutionId"]
    if "TaskExecutionId" in data:
        out["task_execution_id"] = data["TaskExecutionId"]
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "Type" in data:
        import aws_sdk_ssm.types.maintenance_window_task_type

        out["type"] = (
            aws_sdk_ssm.types.maintenance_window_task_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "TaskParameters" in data:
        import aws_sdk_ssm.types.maintenance_window_task_parameters_list

        out["task_parameters"] = (
            aws_sdk_ssm.types.maintenance_window_task_parameters_list.deserialize_aws_json_1_1(
                data["TaskParameters"]
            )
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if "MaxConcurrency" in data:
        out["max_concurrency"] = data["MaxConcurrency"]
    if "MaxErrors" in data:
        out["max_errors"] = data["MaxErrors"]
    if "Status" in data:
        import aws_sdk_ssm.types.maintenance_window_execution_status

        out["status"] = (
            aws_sdk_ssm.types.maintenance_window_execution_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StatusDetails" in data:
        out["status_details"] = data["StatusDetails"]
    if "StartTime" in data:
        import aws_sdk_ssm.types.date_time

        out["start_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_ssm.types.date_time

        out["end_time"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndTime"]
        )
    if "AlarmConfiguration" in data:
        import aws_sdk_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            aws_sdk_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    if "TriggeredAlarms" in data:
        import aws_sdk_ssm.types.alarm_state_information_list

        out["triggered_alarms"] = (
            aws_sdk_ssm.types.alarm_state_information_list.deserialize_aws_json_1_1(
                data["TriggeredAlarms"]
            )
        )
    return out
