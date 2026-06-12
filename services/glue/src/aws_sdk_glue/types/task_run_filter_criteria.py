"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunFilterCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.task_status_type
    import aws_sdk_glue.types.task_type
    import aws_sdk_glue.types.timestamp


class TaskRunFilterCriteria(TypedDict):
    task_run_type: NotRequired["aws_sdk_glue.types.task_type.TaskType"]
    """<p>The type of task run.</p>"""
    status: NotRequired["aws_sdk_glue.types.task_status_type.TaskStatusType"]
    """<p>The current status of the task run.</p>"""
    started_before: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>Filter on task runs started before this date.</p>"""
    started_after: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>Filter on task runs started after this date.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRunFilterCriteria) -> dict:
    out: dict = {}
    if "task_run_type" in value:
        import aws_sdk_glue.types.task_type

        out["TaskRunType"] = aws_sdk_glue.types.task_type.serialize_aws_json_1_1(
            value["task_run_type"]
        )
    if "status" in value:
        import aws_sdk_glue.types.task_status_type

        out["Status"] = aws_sdk_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "started_before" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedBefore"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_before"]
        )
    if "started_after" in value:
        import aws_sdk_glue.types.timestamp

        out["StartedAfter"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_after"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskRunFilterCriteria:
    out: TaskRunFilterCriteria = {}  # type: ignore[typeddict-item]
    if "TaskRunType" in data:
        import aws_sdk_glue.types.task_type

        out["task_run_type"] = aws_sdk_glue.types.task_type.deserialize_aws_json_1_1(
            data["TaskRunType"]
        )
    if "Status" in data:
        import aws_sdk_glue.types.task_status_type

        out["status"] = aws_sdk_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StartedBefore" in data:
        import aws_sdk_glue.types.timestamp

        out["started_before"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedBefore"]
        )
    if "StartedAfter" in data:
        import aws_sdk_glue.types.timestamp

        out["started_after"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedAfter"]
        )
    return out
