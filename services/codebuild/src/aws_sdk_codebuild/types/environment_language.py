"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentLanguage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.environment_images
    import aws_sdk_codebuild.types.language_type


class EnvironmentLanguage(TypedDict):
    language: NotRequired["aws_sdk_codebuild.types.language_type.LanguageType"]
    """<p>The programming language for the Docker images.</p>"""
    images: NotRequired["aws_sdk_codebuild.types.environment_images.EnvironmentImages"]
    """<p>The list of Docker images that are related by the specified programming language.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentLanguage) -> dict:
    out: dict = {}
    if "language" in value:
        import aws_sdk_codebuild.types.language_type

        out["language"] = aws_sdk_codebuild.types.language_type.serialize_aws_json_1_1(
            value["language"]
        )
    if "images" in value:
        import aws_sdk_codebuild.types.environment_images

        out["images"] = (
            aws_sdk_codebuild.types.environment_images.serialize_aws_json_1_1(
                value["images"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentLanguage:
    out: EnvironmentLanguage = {}  # type: ignore[typeddict-item]
    if "language" in data:
        import aws_sdk_codebuild.types.language_type

        out["language"] = (
            aws_sdk_codebuild.types.language_type.deserialize_aws_json_1_1(
                data["language"]
            )
        )
    if "images" in data:
        import aws_sdk_codebuild.types.environment_images

        out["images"] = (
            aws_sdk_codebuild.types.environment_images.deserialize_aws_json_1_1(
                data["images"]
            )
        )
    return out
