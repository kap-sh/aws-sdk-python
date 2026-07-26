"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListWorkflowsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.workflow_summaries


class ListWorkflowsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token returned from a call to this API to indicate the next batch of results to return, if any.</p>"""
    items: NotRequired["capo_codecatalyst.types.workflow_summaries.WorkflowSummaries"]
    """<p>Information about the workflows in a project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkflowsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import capo_codecatalyst.types.workflow_summaries

        out["items"] = capo_codecatalyst.types.workflow_summaries.serialize_json(
            value["items"]
        )
    return out


def deserialize_json(data: dict) -> ListWorkflowsResponse:
    out: ListWorkflowsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import capo_codecatalyst.types.workflow_summaries

        out["items"] = capo_codecatalyst.types.workflow_summaries.deserialize_json(
            data["items"]
        )
    return out
