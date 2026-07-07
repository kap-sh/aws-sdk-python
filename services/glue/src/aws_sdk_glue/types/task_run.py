"""Generated from Smithy shape ``com.amazonaws.glue#TaskRun``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.execution_time
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.task_run_properties
    import aws_sdk_glue.types.task_status_type
    import aws_sdk_glue.types.timestamp


class TaskRun(TypedDict, closed=True):
    transform_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique identifier for the transform.</p>"""
    task_run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique identifier for this task run.</p>"""
    status: NotRequired["aws_sdk_glue.types.task_status_type.TaskStatusType"]
    """<p>The current status of the requested task run.</p>"""
    log_group_name: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The names of the log group for secure logging, associated with this task run.</p>"""
    properties: NotRequired["aws_sdk_glue.types.task_run_properties.TaskRunProperties"]
    """<p>Specifies configuration properties associated with this task run.</p>"""
    error_string: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>The list of error strings associated with this task run.</p>"""
    started_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The date and time that this task run started.</p>"""
    last_modified_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The last point in time that the requested task run was updated.</p>"""
    completed_on: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The last point in time that the requested task run was completed.</p>"""
    execution_time: "aws_sdk_glue.types.execution_time.ExecutionTime"
    """<p>The amount of time (in seconds) that the task run consumed resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRun) -> dict:
    out: dict = {}
    if "transform_id" in value:
        out["TransformId"] = value["transform_id"]
    if "task_run_id" in value:
        out["TaskRunId"] = value["task_run_id"]
    if "status" in value:
        import aws_sdk_glue.types.task_status_type

        out["Status"] = aws_sdk_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "log_group_name" in value:
        out["LogGroupName"] = value["log_group_name"]
    if "properties" in value:
        import aws_sdk_glue.types.task_run_properties

        out["Properties"] = (
            aws_sdk_glue.types.task_run_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "error_string" in value:
        out["ErrorString"] = value["error_string"]
    if "started_on" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_on"]
        )
    if "last_modified_on" in value:
        import aws_sdk_glue.types.timestamp

        out["LastModifiedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_on"]
        )
    if "completed_on" in value:
        import aws_sdk_glue.types.timestamp

        out["CompletedOn"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["completed_on"]
        )
    out["ExecutionTime"] = value.get("execution_time", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskRun:
    out: TaskRun = {}  # type: ignore[typeddict-item]
    if "TransformId" in data:
        out["transform_id"] = data["TransformId"]
    if "TaskRunId" in data:
        out["task_run_id"] = data["TaskRunId"]
    if "Status" in data:
        import aws_sdk_glue.types.task_status_type

        out["status"] = aws_sdk_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "LogGroupName" in data:
        out["log_group_name"] = data["LogGroupName"]
    if "Properties" in data:
        import aws_sdk_glue.types.task_run_properties

        out["properties"] = (
            aws_sdk_glue.types.task_run_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "ErrorString" in data:
        out["error_string"] = data["ErrorString"]
    if "StartedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["started_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedOn"]
        )
    if "LastModifiedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["last_modified_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedOn"]
        )
    if "CompletedOn" in data:
        import aws_sdk_glue.types.timestamp

        out["completed_on"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CompletedOn"]
        )
    if "ExecutionTime" in data:
        out["execution_time"] = data["ExecutionTime"]
    else:
        out["execution_time"] = 0
    return out
