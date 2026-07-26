"""Generated from Smithy shape ``com.amazonaws.datapipeline#TaskObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.id
    import capo_data_pipeline.types.pipeline_object_map
    import capo_data_pipeline.types.task_id


class TaskObject(TypedDict, closed=True):
    task_id: NotRequired["capo_data_pipeline.types.task_id.taskId"]
    """<p>An internal identifier for the task. This ID is passed to the <a>SetTaskStatus</a> and <a>ReportTaskProgress</a> actions.</p>"""
    pipeline_id: NotRequired["capo_data_pipeline.types.id.id"]
    """<p>The ID of the pipeline that provided the task.</p>"""
    attempt_id: NotRequired["capo_data_pipeline.types.id.id"]
    """<p>The ID of the pipeline task attempt object. AWS Data Pipeline uses this value to track how many times a task is attempted.</p>"""
    objects: NotRequired[
        "capo_data_pipeline.types.pipeline_object_map.PipelineObjectMap"
    ]
    """<p>Connection information for the location where the task runner will publish the output of the task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskObject) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "pipeline_id" in value:
        out["pipelineId"] = value["pipeline_id"]
    if "attempt_id" in value:
        out["attemptId"] = value["attempt_id"]
    if "objects" in value:
        import capo_data_pipeline.types.pipeline_object_map

        out["objects"] = (
            capo_data_pipeline.types.pipeline_object_map.serialize_aws_json_1_1(
                value["objects"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskObject:
    out: TaskObject = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    if "attemptId" in data:
        out["attempt_id"] = data["attemptId"]
    if "objects" in data:
        import capo_data_pipeline.types.pipeline_object_map

        out["objects"] = (
            capo_data_pipeline.types.pipeline_object_map.deserialize_aws_json_1_1(
                data["objects"]
            )
        )
    return out
