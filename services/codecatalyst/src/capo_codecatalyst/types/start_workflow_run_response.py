"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StartWorkflowRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.name_string
    import capo_codecatalyst.types.uuid


class StartWorkflowRunResponse(TypedDict, closed=True):
    space_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "capo_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the workflow run.</p>"""
    workflow_id: "capo_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the workflow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartWorkflowRunResponse) -> dict:
    out: dict = {}
    out["spaceName"] = value["space_name"]
    out["projectName"] = value["project_name"]
    out["id"] = value["id"]
    out["workflowId"] = value["workflow_id"]
    return out


def deserialize_json(data: dict) -> StartWorkflowRunResponse:
    out: StartWorkflowRunResponse = {}  # type: ignore[typeddict-item]
    if "spaceName" in data:
        out["space_name"] = data["spaceName"]
    else:
        raise DeserializationError("StartWorkflowRunResponse.space_name required")
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("StartWorkflowRunResponse.project_name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartWorkflowRunResponse.id required")
    if "workflowId" in data:
        out["workflow_id"] = data["workflowId"]
    else:
        raise DeserializationError("StartWorkflowRunResponse.workflow_id required")
    return out
