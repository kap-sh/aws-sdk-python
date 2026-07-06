"""Generated from Smithy shape ``com.amazonaws.groundstation#GetAgentConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class GetAgentConfigurationResponse(TypedDict, closed=True):
    agent_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>UUID of agent.</p>"""
    tasking_document: NotRequired["str"]
    """<p>Tasking document for agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentConfigurationResponse) -> dict:
    out: dict = {}
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    if "tasking_document" in value:
        out["taskingDocument"] = value["tasking_document"]
    return out


def deserialize_json(data: dict) -> GetAgentConfigurationResponse:
    out: GetAgentConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    if "taskingDocument" in data:
        out["tasking_document"] = data["taskingDocument"]
    return out
