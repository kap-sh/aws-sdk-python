"""Generated from Smithy shape ``com.amazonaws.amplify#GetArtifactUrlResult``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplify.types.artifact_id
    import aws_sdk_amplify.types.artifact_url


class GetArtifactUrlResult(TypedDict):
    artifact_id: "aws_sdk_amplify.types.artifact_id.ArtifactId"
    """<p>The unique ID for an artifact. </p>"""
    artifact_url: "aws_sdk_amplify.types.artifact_url.ArtifactUrl"
    """<p>The presigned URL for the artifact. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetArtifactUrlResult) -> dict:
    out: dict = {}
    out["artifactId"] = value["artifact_id"]
    out["artifactUrl"] = value["artifact_url"]
    return out


def deserialize_json(data: dict) -> GetArtifactUrlResult:
    out: GetArtifactUrlResult = {}  # type: ignore[typeddict-item]
    if "artifactId" in data:
        out["artifact_id"] = data["artifactId"]
    else:
        raise DeserializationError("GetArtifactUrlResult.artifact_id required")
    if "artifactUrl" in data:
        out["artifact_url"] = data["artifactUrl"]
    else:
        raise DeserializationError("GetArtifactUrlResult.artifact_url required")
    return out
