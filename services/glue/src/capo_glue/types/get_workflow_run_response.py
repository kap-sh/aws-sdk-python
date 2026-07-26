"""Generated from Smithy shape ``com.amazonaws.glue#GetWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.workflow_run


class GetWorkflowRunResponse(TypedDict, closed=True):
    run: NotRequired["capo_glue.types.workflow_run.WorkflowRun"]
    """<p>The requested workflow run metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWorkflowRunResponse) -> dict:
    out: dict = {}
    if "run" in value:
        import capo_glue.types.workflow_run

        out["Run"] = capo_glue.types.workflow_run.serialize_aws_json_1_1(value["run"])
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWorkflowRunResponse:
    out: GetWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "Run" in data:
        import capo_glue.types.workflow_run

        out["run"] = capo_glue.types.workflow_run.deserialize_aws_json_1_1(data["Run"])
    return out
