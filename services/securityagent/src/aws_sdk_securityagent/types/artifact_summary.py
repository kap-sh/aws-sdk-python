"""Generated from Smithy shape ``com.amazonaws.securityagent#ArtifactSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.artifact_id
    import aws_sdk_securityagent.types.artifact_type


class ArtifactSummary(TypedDict):
    artifact_id: "aws_sdk_securityagent.types.artifact_id.ArtifactId"
    """<p>The unique identifier of the artifact.</p>"""
    file_name: "str"
    """<p>The file name of the artifact.</p>"""
    artifact_type: "aws_sdk_securityagent.types.artifact_type.ArtifactType"
    """<p>The file type of the artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactSummary) -> dict:
    out: dict = {}
    out["artifactId"] = value["artifact_id"]
    out["fileName"] = value["file_name"]
    import aws_sdk_securityagent.types.artifact_type

    out["artifactType"] = aws_sdk_securityagent.types.artifact_type.serialize_json(
        value["artifact_type"]
    )
    return out


def deserialize_json(data: dict) -> ArtifactSummary:
    out: ArtifactSummary = {}  # type: ignore[typeddict-item]
    if "artifactId" in data:
        out["artifact_id"] = data["artifactId"]
    else:
        raise DeserializationError("ArtifactSummary.artifact_id required")
    if "fileName" in data:
        out["file_name"] = data["fileName"]
    else:
        raise DeserializationError("ArtifactSummary.file_name required")
    if "artifactType" in data:
        import aws_sdk_securityagent.types.artifact_type

        out["artifact_type"] = (
            aws_sdk_securityagent.types.artifact_type.deserialize_json(
                data["artifactType"]
            )
        )
    else:
        raise DeserializationError("ArtifactSummary.artifact_type required")
    return out
