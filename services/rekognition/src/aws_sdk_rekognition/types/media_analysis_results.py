"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisResults``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.media_analysis_model_versions
    import aws_sdk_rekognition.types.s3_object


class MediaAnalysisResults(TypedDict, closed=True):
    s3_object: NotRequired["aws_sdk_rekognition.types.s3_object.S3Object"]
    model_versions: NotRequired[
        "aws_sdk_rekognition.types.media_analysis_model_versions.MediaAnalysisModelVersions"
    ]
    """<p>Information about the model versions for the features selected in a given job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisResults) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import aws_sdk_rekognition.types.s3_object

        out["S3Object"] = aws_sdk_rekognition.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    if "model_versions" in value:
        import aws_sdk_rekognition.types.media_analysis_model_versions

        out["ModelVersions"] = (
            aws_sdk_rekognition.types.media_analysis_model_versions.serialize_aws_json_1_1(
                value["model_versions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisResults:
    out: MediaAnalysisResults = {}  # type: ignore[typeddict-item]
    if "S3Object" in data:
        import aws_sdk_rekognition.types.s3_object

        out["s3_object"] = aws_sdk_rekognition.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    if "ModelVersions" in data:
        import aws_sdk_rekognition.types.media_analysis_model_versions

        out["model_versions"] = (
            aws_sdk_rekognition.types.media_analysis_model_versions.deserialize_aws_json_1_1(
                data["ModelVersions"]
            )
        )
    return out
