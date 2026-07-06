"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_location_type
    import aws_sdk_codepipeline.types.s3_artifact_location


class ArtifactLocation(TypedDict, closed=True):
    type: NotRequired[
        "aws_sdk_codepipeline.types.artifact_location_type.ArtifactLocationType"
    ]
    """<p>The type of artifact in the location.</p>"""
    s3_location: NotRequired[
        "aws_sdk_codepipeline.types.s3_artifact_location.S3ArtifactLocation"
    ]
    """<p>The S3 bucket that contains the artifact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactLocation) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_codepipeline.types.artifact_location_type

        out["type"] = (
            aws_sdk_codepipeline.types.artifact_location_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "s3_location" in value:
        import aws_sdk_codepipeline.types.s3_artifact_location

        out["s3Location"] = (
            aws_sdk_codepipeline.types.s3_artifact_location.serialize_aws_json_1_1(
                value["s3_location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactLocation:
    out: ArtifactLocation = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_codepipeline.types.artifact_location_type

        out["type"] = (
            aws_sdk_codepipeline.types.artifact_location_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "s3Location" in data:
        import aws_sdk_codepipeline.types.s3_artifact_location

        out["s3_location"] = (
            aws_sdk_codepipeline.types.s3_artifact_location.deserialize_aws_json_1_1(
                data["s3Location"]
            )
        )
    return out
