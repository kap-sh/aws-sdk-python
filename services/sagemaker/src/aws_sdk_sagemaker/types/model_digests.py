"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelDigests``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_digest


class ModelDigests(TypedDict, closed=True):
    artifact_digest: NotRequired[
        "aws_sdk_sagemaker.types.artifact_digest.ArtifactDigest"
    ]
    """<p>Provides a hash value that uniquely identifies the stored model artifacts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelDigests) -> dict:
    out: dict = {}
    if "artifact_digest" in value:
        out["ArtifactDigest"] = value["artifact_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelDigests:
    out: ModelDigests = {}  # type: ignore[typeddict-item]
    if "ArtifactDigest" in data:
        out["artifact_digest"] = data["ArtifactDigest"]
    return out
