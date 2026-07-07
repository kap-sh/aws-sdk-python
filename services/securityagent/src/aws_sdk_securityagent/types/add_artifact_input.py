"""Generated from Smithy shape ``com.amazonaws.securityagent#AddArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.agent_space_id
    import aws_sdk_securityagent.types.artifact_type


class AddArtifactInput(TypedDict, closed=True):
    agent_space_id: "aws_sdk_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space to add the artifact to.</p>"""
    artifact_content: "bytes"
    """<p>The binary content of the artifact to upload.</p>"""
    artifact_type: "aws_sdk_securityagent.types.artifact_type.ArtifactType"
    """<p>The file type of the artifact. Valid values include TXT, PNG, JPEG, MD, PDF, DOCX, DOC, JSON, and YAML.</p>"""
    file_name: "str"
    """<p>The file name of the artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddArtifactInput) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    import aws_sdk_securityagent.types._prelude.blob

    out["artifactContent"] = aws_sdk_securityagent.types._prelude.blob.serialize_json(
        value["artifact_content"]
    )
    import aws_sdk_securityagent.types.artifact_type

    out["artifactType"] = aws_sdk_securityagent.types.artifact_type.serialize_json(
        value["artifact_type"]
    )
    out["fileName"] = value["file_name"]
    return out


def deserialize_json(data: dict) -> AddArtifactInput:
    out: AddArtifactInput = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("AddArtifactInput.agent_space_id required")
    if "artifactContent" in data:
        import aws_sdk_securityagent.types._prelude.blob

        out["artifact_content"] = (
            aws_sdk_securityagent.types._prelude.blob.deserialize_json(
                data["artifactContent"]
            )
        )
    else:
        raise DeserializationError("AddArtifactInput.artifact_content required")
    if "artifactType" in data:
        import aws_sdk_securityagent.types.artifact_type

        out["artifact_type"] = (
            aws_sdk_securityagent.types.artifact_type.deserialize_json(
                data["artifactType"]
            )
        )
    else:
        raise DeserializationError("AddArtifactInput.artifact_type required")
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("AddArtifactInput.file_name required")
    return out
