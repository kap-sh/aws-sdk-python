"""Generated from Smithy shape ``com.amazonaws.datapipeline#PollForTaskOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.task_object


class PollForTaskOutput(TypedDict, closed=True):
    task_object: NotRequired["capo_data_pipeline.types.task_object.TaskObject"]
    """<p>The information needed to complete the task that is being assigned to the task runner. One of the fields returned in this object is <code>taskId</code>, which contains an identifier for the task being assigned. The calling task runner uses <code>taskId</code> in subsequent calls to <a>ReportTaskProgress</a> and <a>SetTaskStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollForTaskOutput) -> dict:
    out: dict = {}
    if "task_object" in value:
        import capo_data_pipeline.types.task_object

        out["taskObject"] = capo_data_pipeline.types.task_object.serialize_aws_json_1_1(
            value["task_object"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PollForTaskOutput:
    out: PollForTaskOutput = {}  # type: ignore[typeddict-item]
    if "taskObject" in data:
        import capo_data_pipeline.types.task_object

        out["task_object"] = (
            capo_data_pipeline.types.task_object.deserialize_aws_json_1_1(
                data["taskObject"]
            )
        )
    return out
