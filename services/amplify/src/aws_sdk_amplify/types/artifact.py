"""Generated from Smithy shape ``com.amazonaws.amplify#Artifact``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.artifact_file_name
    import aws_sdk_amplify.types.artifact_id


class Artifact(TypedDict):
    artifact_file_name: "aws_sdk_amplify.types.artifact_file_name.ArtifactFileName"
    """<p>The file name for the artifact. </p>"""
    artifact_id: "aws_sdk_amplify.types.artifact_id.ArtifactId"
    """<p>The unique ID for the artifact. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Artifact) -> dict:
    out: dict = {}
    out["artifactFileName"] = value["artifact_file_name"]
    out["artifactId"] = value["artifact_id"]
    return out


def deserialize_json(data: dict) -> Artifact:
    out: Artifact = {}  # type: ignore[typeddict-item]
    if "artifactFileName" in data:
        out["artifact_file_name"] = data["artifactFileName"]
    else:
        raise DeserializationError("Artifact.artifact_file_name required")
    if "artifactId" in data:
        out["artifact_id"] = data["artifactId"]
    else:
        raise DeserializationError("Artifact.artifact_id required")
    return out
