"""Generated from Smithy shape ``com.amazonaws.securityagent#DeleteArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.artifact_id


class DeleteArtifactInput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space that contains the artifact.</p>"""
    artifact_id: "capo_securityagent.types.artifact_id.ArtifactId"
    """<p>The unique identifier of the artifact to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteArtifactInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["artifactId"] = value["artifact_id"]
    return out


def deserialize_json(data: dict) -> DeleteArtifactInput:
    out: DeleteArtifactInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("DeleteArtifactInput.agent_space_id required")
    if "artifactId" in data:
        out["artifact_id"] = data["artifactId"]
    else:
        raise DeserializationError("DeleteArtifactInput.artifact_id required")
    return out
