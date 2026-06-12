"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentPlatform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.environment_languages
    import aws_sdk_codebuild.types.platform_type


class EnvironmentPlatform(TypedDict):
    platform: NotRequired["aws_sdk_codebuild.types.platform_type.PlatformType"]
    """<p>The platform's name.</p>"""
    languages: NotRequired[
        "aws_sdk_codebuild.types.environment_languages.EnvironmentLanguages"
    ]
    """<p>The list of programming languages that are available for the specified platform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentPlatform) -> dict:
    out: dict = {}
    if "platform" in value:
        import aws_sdk_codebuild.types.platform_type

        out["platform"] = aws_sdk_codebuild.types.platform_type.serialize_aws_json_1_1(
            value["platform"]
        )
    if "languages" in value:
        import aws_sdk_codebuild.types.environment_languages

        out["languages"] = (
            aws_sdk_codebuild.types.environment_languages.serialize_aws_json_1_1(
                value["languages"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentPlatform:
    out: EnvironmentPlatform = {}  # type: ignore[typeddict-item]
    if "platform" in data:
        import aws_sdk_codebuild.types.platform_type

        out["platform"] = (
            aws_sdk_codebuild.types.platform_type.deserialize_aws_json_1_1(
                data["platform"]
            )
        )
    if "languages" in data:
        import aws_sdk_codebuild.types.environment_languages

        out["languages"] = (
            aws_sdk_codebuild.types.environment_languages.deserialize_aws_json_1_1(
                data["languages"]
            )
        )
    return out
