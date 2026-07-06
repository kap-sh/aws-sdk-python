"""Generated from Smithy shape ``com.amazonaws.securityagent#BatchGetArtifactMetadataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_id
    import aws_sdk_securityagent.types.artifact_ids


class BatchGetArtifactMetadataInput(TypedDict, closed=True):
    agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space that contains the artifacts.</p>"""
    artifact_ids: "aws_sdk_securityagent.types.artifact_ids.ArtifactIds"
    """<p>The list of artifact identifiers to retrieve metadata for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetArtifactMetadataInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import aws_sdk_securityagent.types.artifact_ids

    out["artifactIds"] = aws_sdk_securityagent.types.artifact_ids.serialize_json(
        value["artifact_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetArtifactMetadataInput:
    out: BatchGetArtifactMetadataInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "BatchGetArtifactMetadataInput.agent_space_id required"
        )
    if "artifactIds" in data:
        import aws_sdk_securityagent.types.artifact_ids

        out["artifact_ids"] = aws_sdk_securityagent.types.artifact_ids.deserialize_json(
            data["artifactIds"]
        )
    else:
        raise DeserializationError(
            "BatchGetArtifactMetadataInput.artifact_ids required"
        )
    return out
