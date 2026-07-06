"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_name
    import aws_sdk_codepipeline.types.s3_location


class ArtifactDetail(TypedDict, closed=True):
    name: NotRequired["aws_sdk_codepipeline.types.artifact_name.ArtifactName"]
    """<p>The artifact object name for the action execution.</p>"""
    s3location: NotRequired["aws_sdk_codepipeline.types.s3_location.S3Location"]
    """<p>The Amazon S3 artifact location for the action execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactDetail) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "s3location" in value:
        import aws_sdk_codepipeline.types.s3_location

        out["s3location"] = (
            aws_sdk_codepipeline.types.s3_location.serialize_aws_json_1_1(
                value["s3location"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactDetail:
    out: ArtifactDetail = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "s3location" in data:
        import aws_sdk_codepipeline.types.s3_location

        out["s3location"] = (
            aws_sdk_codepipeline.types.s3_location.deserialize_aws_json_1_1(
                data["s3location"]
            )
        )
    return out
