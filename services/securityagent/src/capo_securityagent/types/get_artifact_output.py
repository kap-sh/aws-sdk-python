"""Generated from Smithy shape ``com.amazonaws.securityagent#GetArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.agent_space_id
    import capo_securityagent.types.artifact
    import capo_securityagent.types.artifact_id


class GetArtifactOutput(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space that contains the artifact.</p>"""
    artifact_id: "capo_securityagent.types.artifact_id.ArtifactId"
    """<p>The unique identifier of the artifact.</p>"""
    artifact: "capo_securityagent.types.artifact.Artifact"
    """<p>The artifact content and type.</p>"""
    file_name: "str"
    """<p>The file name of the artifact.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time the artifact was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetArtifactOutput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["artifactId"] = value["artifact_id"]
    import capo_securityagent.types.artifact

    out["artifact"] = capo_securityagent.types.artifact.serialize_json(
        value["artifact"]
    )
    out["fileName"] = value["file_name"]
    import capo_securityagent.types._prelude.timestamp

    out["updatedAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> GetArtifactOutput:
    out: GetArtifactOutput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("GetArtifactOutput.agent_space_id required")
    if "artifactId" in data:
        out["artifact_id"] = data["artifactId"]
    else:
        raise DeserializationError("GetArtifactOutput.artifact_id required")
    if "artifact" in data:
        import capo_securityagent.types.artifact

        out["artifact"] = capo_securityagent.types.artifact.deserialize_json(
            data["artifact"]
        )
    else:
        raise DeserializationError("GetArtifactOutput.artifact required")
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("GetArtifactOutput.file_name required")
    if "updatedAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("GetArtifactOutput.updated_at required")
    return out
