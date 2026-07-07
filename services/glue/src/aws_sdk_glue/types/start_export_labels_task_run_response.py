"""Generated from Smithy shape ``com.amazonaws.glue#StartExportLabelsTaskRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.hash_string


class StartExportLabelsTaskRunResponse(TypedDict, closed=True):
    task_run_id: NotRequired["aws_sdk_glue.types.hash_string.HashString"]
    """<p>The unique identifier for the task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartExportLabelsTaskRunResponse) -> dict:
    out: dict = {}
    if "task_run_id" in value:
        out["TaskRunId"] = value["task_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartExportLabelsTaskRunResponse:
    out: StartExportLabelsTaskRunResponse = {}  # type: ignore[typeddict-item]
    if "TaskRunId" in data:
        out["task_run_id"] = data["TaskRunId"]
    return out
