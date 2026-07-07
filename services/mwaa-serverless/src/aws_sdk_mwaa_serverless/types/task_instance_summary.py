"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#TaskInstanceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.generic_string
    import aws_sdk_mwaa_serverless.types.id_string
    import aws_sdk_mwaa_serverless.types.task_instance_status
    import aws_sdk_mwaa_serverless.types.version_id
    import aws_sdk_mwaa_serverless.types.workflow_arn


class TaskInstanceSummary(TypedDict, closed=True):
    workflow_arn: NotRequired["aws_sdk_mwaa_serverless.types.workflow_arn.WorkflowArn"]
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this task instance.</p>"""
    workflow_version: NotRequired["aws_sdk_mwaa_serverless.types.version_id.VersionId"]
    """<p>The version of the workflow that contains this task instance.</p>"""
    run_id: NotRequired["aws_sdk_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of the workflow run that contains this task instance.</p>"""
    task_instance_id: NotRequired["aws_sdk_mwaa_serverless.types.id_string.IdString"]
    """<p>The unique identifier of this task instance.</p>"""
    status: NotRequired[
        "aws_sdk_mwaa_serverless.types.task_instance_status.TaskInstanceStatus"
    ]
    """<p>The current status of the task instance.</p>"""
    duration_in_seconds: NotRequired["int"]
    """<p>The duration of the task instance execution in seconds. This value is null if the task is not complete.</p>"""
    operator_name: NotRequired[
        "aws_sdk_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The name of the Apache Airflow operator used for this task instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskInstanceSummary) -> dict:
    out: dict = {}
    if "workflow_arn" in value:
        out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    if "task_instance_id" in value:
        out["TaskInstanceId"] = value["task_instance_id"]
    if "status" in value:
        import aws_sdk_mwaa_serverless.types.task_instance_status

        out["Status"] = (
            aws_sdk_mwaa_serverless.types.task_instance_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    if "operator_name" in value:
        out["OperatorName"] = value["operator_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskInstanceSummary:
    out: TaskInstanceSummary = {}  # type: ignore[typeddict-item]
    if "WorkflowArn" in data:
        out["workflow_arn"] = data["WorkflowArn"]
    if "WorkflowVersion" in data:
        out["workflow_version"] = data["WorkflowVersion"]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    if "TaskInstanceId" in data:
        out["task_instance_id"] = data["TaskInstanceId"]
    if "Status" in data:
        import aws_sdk_mwaa_serverless.types.task_instance_status

        out["status"] = (
            aws_sdk_mwaa_serverless.types.task_instance_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    if "OperatorName" in data:
        out["operator_name"] = data["OperatorName"]
    return out
