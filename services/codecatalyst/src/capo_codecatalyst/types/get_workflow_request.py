"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class GetWorkflowRequest(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The ID of the workflow. To rerieve a list of workflow IDs, use <a>ListWorkflows</a>.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkflowRequest:
    out: GetWorkflowRequest = {}  # type: ignore[typeddict-item]
    return out
