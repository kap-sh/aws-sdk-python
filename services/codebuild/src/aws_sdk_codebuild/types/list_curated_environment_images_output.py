"""Generated from Smithy shape ``com.amazonaws.codebuild#ListCuratedEnvironmentImagesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.environment_platforms


class ListCuratedEnvironmentImagesOutput(TypedDict, closed=True):
    platforms: NotRequired[
        "aws_sdk_codebuild.types.environment_platforms.EnvironmentPlatforms"
    ]
    """<p>Information about supported platforms for Docker images that are managed by CodeBuild.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCuratedEnvironmentImagesOutput) -> dict:
    out: dict = {}
    if "platforms" in value:
        import aws_sdk_codebuild.types.environment_platforms

        out["platforms"] = (
            aws_sdk_codebuild.types.environment_platforms.serialize_aws_json_1_1(
                value["platforms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCuratedEnvironmentImagesOutput:
    out: ListCuratedEnvironmentImagesOutput = {}  # type: ignore[typeddict-item]
    if "platforms" in data:
        import aws_sdk_codebuild.types.environment_platforms

        out["platforms"] = (
            aws_sdk_codebuild.types.environment_platforms.deserialize_aws_json_1_1(
                data["platforms"]
            )
        )
    return out
