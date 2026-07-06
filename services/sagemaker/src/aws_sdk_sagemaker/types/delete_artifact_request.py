"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteArtifactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.artifact_arn
    import aws_sdk_sagemaker.types.artifact_source


class DeleteArtifactRequest(TypedDict, closed=True):
    artifact_arn: NotRequired["aws_sdk_sagemaker.types.artifact_arn.ArtifactArn"]
    """<p>The Amazon Resource Name (ARN) of the artifact to delete.</p>"""
    source: NotRequired["aws_sdk_sagemaker.types.artifact_source.ArtifactSource"]
    """<p>The URI of the source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteArtifactRequest) -> dict:
    out: dict = {}
    if "artifact_arn" in value:
        out["ArtifactArn"] = value["artifact_arn"]
    if "source" in value:
        import aws_sdk_sagemaker.types.artifact_source

        out["Source"] = aws_sdk_sagemaker.types.artifact_source.serialize_aws_json_1_1(
            value["source"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteArtifactRequest:
    out: DeleteArtifactRequest = {}  # type: ignore[typeddict-item]
    if "ArtifactArn" in data:
        out["artifact_arn"] = data["ArtifactArn"]
    if "Source" in data:
        import aws_sdk_sagemaker.types.artifact_source

        out["source"] = (
            aws_sdk_sagemaker.types.artifact_source.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    return out
