"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateMaintenanceWindowTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm_configuration
    import aws_sdk_ssm.types.logging_info
    import aws_sdk_ssm.types.maintenance_window_description
    import aws_sdk_ssm.types.maintenance_window_id
    import aws_sdk_ssm.types.maintenance_window_name
    import aws_sdk_ssm.types.maintenance_window_task_arn
    import aws_sdk_ssm.types.maintenance_window_task_cutoff_behavior
    import aws_sdk_ssm.types.maintenance_window_task_id
    import aws_sdk_ssm.types.maintenance_window_task_invocation_parameters
    import aws_sdk_ssm.types.maintenance_window_task_parameters
    import aws_sdk_ssm.types.maintenance_window_task_priority
    import aws_sdk_ssm.types.max_concurrency
    import aws_sdk_ssm.types.max_errors
    import aws_sdk_ssm.types.service_role
    import aws_sdk_ssm.types.targets


class UpdateMaintenanceWindowTaskResult(TypedDict, closed=True):
    window_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_id.MaintenanceWindowId"
    ]
    """<p>The ID of the maintenance window that was updated.</p>"""
    window_task_id: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId"
    ]
    """<p>The task ID of the maintenance window that was updated.</p>"""
    targets: NotRequired["aws_sdk_ssm.types.targets.Targets"]
    """<p>The updated target values.</p>"""
    task_arn: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_arn.MaintenanceWindowTaskArn"
    ]
    """<p>The updated task ARN value.</p>"""
    service_role_arn: NotRequired["aws_sdk_ssm.types.service_role.ServiceRole"]
    r"""<p>The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run <code>RegisterTaskWithMaintenanceWindow</code>.</p> <p>However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see <a href=\"https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html\">Setting up Maintenance Windows</a> in the in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    task_parameters: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_parameters.MaintenanceWindowTaskParameters"
    ]
    """<p>The updated parameter values.</p> <note> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note>"""
    task_invocation_parameters: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_invocation_parameters.MaintenanceWindowTaskInvocationParameters"
    ]
    """<p>The updated parameter values.</p>"""
    priority: "aws_sdk_ssm.types.maintenance_window_task_priority.MaintenanceWindowTaskPriority"
    """<p>The updated priority value.</p>"""
    max_concurrency: NotRequired["aws_sdk_ssm.types.max_concurrency.MaxConcurrency"]
    """<p>The updated <code>MaxConcurrency</code> value.</p>"""
    max_errors: NotRequired["aws_sdk_ssm.types.max_errors.MaxErrors"]
    """<p>The updated <code>MaxErrors</code> value.</p>"""
    logging_info: NotRequired["aws_sdk_ssm.types.logging_info.LoggingInfo"]
    """<p>The updated logging information in Amazon S3.</p> <note> <p> <code>LoggingInfo</code> has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the <code>OutputS3BucketName</code> and <code>OutputS3KeyPrefix</code> options in the <code>TaskInvocationParameters</code> structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note>"""
    name: NotRequired["aws_sdk_ssm.types.maintenance_window_name.MaintenanceWindowName"]
    """<p>The updated task name.</p>"""
    description: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
    ]
    """<p>The updated task description.</p>"""
    cutoff_behavior: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_task_cutoff_behavior.MaintenanceWindowTaskCutoffBehavior"
    ]
    """<p>The specification for whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached. </p>"""
    alarm_configuration: NotRequired[
        "aws_sdk_ssm.types.alarm_configuration.AlarmConfiguration"
    ]
    """<p>The details for the CloudWatch alarm you applied to your maintenance window task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMaintenanceWindowTaskResult) -> dict:
    out: dict = {}
    if "window_id" in value:
        out["WindowId"] = value["window_id"]
    if "window_task_id" in value:
        out["WindowTaskId"] = value["window_task_id"]
    if "targets" in value:
        import aws_sdk_ssm.types.targets

        out["Targets"] = aws_sdk_ssm.types.targets.serialize_aws_json_1_1(
            value["targets"]
        )
    if "task_arn" in value:
        out["TaskArn"] = value["task_arn"]
    if "service_role_arn" in value:
        out["ServiceRoleArn"] = value["service_role_arn"]
    if "task_parameters" in value:
        import aws_sdk_ssm.types.maintenance_window_task_parameters

        out["TaskParameters"] = (
            aws_sdk_ssm.types.maintenance_window_task_parameters.serialize_aws_json_1_1(
                value["task_parameters"]
            )
        )
    if "task_invocation_parameters" in value:
        import aws_sdk_ssm.types.maintenance_window_task_invocation_parameters

        out["TaskInvocationParameters"] = (
            aws_sdk_ssm.types.maintenance_window_task_invocation_parameters.serialize_aws_json_1_1(
                value["task_invocation_parameters"]
            )
        )
    out["Priority"] = value.get("priority", 0)
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "max_errors" in value:
        out["MaxErrors"] = value["max_errors"]
    if "logging_info" in value:
        import aws_sdk_ssm.types.logging_info

        out["LoggingInfo"] = aws_sdk_ssm.types.logging_info.serialize_aws_json_1_1(
            value["logging_info"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "cutoff_behavior" in value:
        import aws_sdk_ssm.types.maintenance_window_task_cutoff_behavior

        out["CutoffBehavior"] = (
            aws_sdk_ssm.types.maintenance_window_task_cutoff_behavior.serialize_aws_json_1_1(
                value["cutoff_behavior"]
            )
        )
    if "alarm_configuration" in value:
        import aws_sdk_ssm.types.alarm_configuration

        out["AlarmConfiguration"] = (
            aws_sdk_ssm.types.alarm_configuration.serialize_aws_json_1_1(
                value["alarm_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMaintenanceWindowTaskResult:
    out: UpdateMaintenanceWindowTaskResult = {}  # type: ignore[typeddict-item]
    if "WindowId" in data:
        out["window_id"] = data["WindowId"]
    if "WindowTaskId" in data:
        out["window_task_id"] = data["WindowTaskId"]
    if "Targets" in data:
        import aws_sdk_ssm.types.targets

        out["targets"] = aws_sdk_ssm.types.targets.deserialize_aws_json_1_1(
            data["Targets"]
        )
    if "TaskArn" in data:
        out["task_arn"] = data["TaskArn"]
    if "ServiceRoleArn" in data:
        out["service_role_arn"] = data["ServiceRoleArn"]
    if "TaskParameters" in data:
        import aws_sdk_ssm.types.maintenance_window_task_parameters

        out["task_parameters"] = (
            aws_sdk_ssm.types.maintenance_window_task_parameters.deserialize_aws_json_1_1(
                data["TaskParameters"]
            )
        )
    if "TaskInvocationParameters" in data:
        import aws_sdk_ssm.types.maintenance_window_task_invocation_parameters

        out["task_invocation_parameters"] = (
            aws_sdk_ssm.types.maintenance_window_task_invocation_parameters.deserialize_aws_json_1_1(
                data["TaskInvocationParameters"]
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
    if "LoggingInfo" in data:
        import aws_sdk_ssm.types.logging_info

        out["logging_info"] = aws_sdk_ssm.types.logging_info.deserialize_aws_json_1_1(
            data["LoggingInfo"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CutoffBehavior" in data:
        import aws_sdk_ssm.types.maintenance_window_task_cutoff_behavior

        out["cutoff_behavior"] = (
            aws_sdk_ssm.types.maintenance_window_task_cutoff_behavior.deserialize_aws_json_1_1(
                data["CutoffBehavior"]
            )
        )
    if "AlarmConfiguration" in data:
        import aws_sdk_ssm.types.alarm_configuration

        out["alarm_configuration"] = (
            aws_sdk_ssm.types.alarm_configuration.deserialize_aws_json_1_1(
                data["AlarmConfiguration"]
            )
        )
    return out
