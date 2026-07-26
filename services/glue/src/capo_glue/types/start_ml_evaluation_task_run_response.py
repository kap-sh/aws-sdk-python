"""Generated from Smithy shape ``com.amazonaws.glue#StartMLEvaluationTaskRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class StartMLEvaluationTaskRunResponse(TypedDict, closed=True):
    task_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The unique identifier associated with this run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMLEvaluationTaskRunResponse) -> dict:
    out: dict = {}
    if "task_run_id" in value:
        out["TaskRunId"] = value["task_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMLEvaluationTaskRunResponse:
    out: StartMLEvaluationTaskRunResponse = {}  # type: ignore[typeddict-item]
    if "TaskRunId" in data:
        out["task_run_id"] = data["TaskRunId"]
    return out
