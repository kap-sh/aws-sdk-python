"""Generated from Smithy shape ``com.amazonaws.glue#StartWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.id_string


class StartWorkflowRunResponse(TypedDict, closed=True):
    run_id: NotRequired["capo_glue.types.id_string.IdString"]
    """<p>An Id for the new run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartWorkflowRunResponse) -> dict:
    out: dict = {}
    if "run_id" in value:
        out["RunId"] = value["run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartWorkflowRunResponse:
    out: StartWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "RunId" in data:
        out["run_id"] = data["RunId"]
    return out
