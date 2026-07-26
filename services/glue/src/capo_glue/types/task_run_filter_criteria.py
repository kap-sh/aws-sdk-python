"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.task_status_type
    import capo_glue.types.task_type
    import capo_glue.types.timestamp


class TaskRunFilterCriteria(TypedDict, closed=True):
    task_run_type: NotRequired["capo_glue.types.task_type.TaskType"]
    """<p>The type of task run.</p>"""
    status: NotRequired["capo_glue.types.task_status_type.TaskStatusType"]
    """<p>The current status of the task run.</p>"""
    started_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter on task runs started before this date.</p>"""
    started_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter on task runs started after this date.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRunFilterCriteria) -> dict:
    out: dict = {}
    if "task_run_type" in value:
        import capo_glue.types.task_type

        out["TaskRunType"] = capo_glue.types.task_type.serialize_aws_json_1_1(
            value["task_run_type"]
        )
    if "status" in value:
        import capo_glue.types.task_status_type

        out["Status"] = capo_glue.types.task_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "started_before" in value:
        import capo_glue.types.timestamp

        out["StartedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_before"]
        )
    if "started_after" in value:
        import capo_glue.types.timestamp

        out["StartedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["started_after"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskRunFilterCriteria:
    out: TaskRunFilterCriteria = {}  # type: ignore[typeddict-item]
    if "TaskRunType" in data:
        import capo_glue.types.task_type

        out["task_run_type"] = capo_glue.types.task_type.deserialize_aws_json_1_1(
            data["TaskRunType"]
        )
    if "Status" in data:
        import capo_glue.types.task_status_type

        out["status"] = capo_glue.types.task_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StartedBefore" in data:
        import capo_glue.types.timestamp

        out["started_before"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedBefore"]
        )
    if "StartedAfter" in data:
        import capo_glue.types.timestamp

        out["started_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["StartedAfter"]
        )
    return out
