"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentImage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.image_versions
    import aws_sdk_codebuild.types.string


class EnvironmentImage(TypedDict):
    name: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The name of the Docker image.</p>"""
    description: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The description of the Docker image.</p>"""
    versions: NotRequired["aws_sdk_codebuild.types.image_versions.ImageVersions"]
    """<p>A list of environment image versions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentImage) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "versions" in value:
        import aws_sdk_codebuild.types.image_versions

        out["versions"] = aws_sdk_codebuild.types.image_versions.serialize_aws_json_1_1(
            value["versions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentImage:
    out: EnvironmentImage = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "versions" in data:
        import aws_sdk_codebuild.types.image_versions

        out["versions"] = (
            aws_sdk_codebuild.types.image_versions.deserialize_aws_json_1_1(
                data["versions"]
            )
        )
    return out
