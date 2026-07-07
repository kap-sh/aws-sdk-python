"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteArtifactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_arn


class DeleteArtifactResponse(TypedDict, closed=True):
    artifact_arn: NotRequired["aws_sdk_sagemaker.types.artifact_arn.ArtifactArn"]
    """<p>The Amazon Resource Name (ARN) of the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteArtifactResponse) -> dict:
    out: dict = {}
    if "artifact_arn" in value:
        out["ArtifactArn"] = value["artifact_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteArtifactResponse:
    out: DeleteArtifactResponse = {}  # type: ignore[typeddict-item]
    if "ArtifactArn" in data:
        out["artifact_arn"] = data["ArtifactArn"]
    return out
