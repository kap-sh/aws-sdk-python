"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentPlatforms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.environment_platform

EnvironmentPlatforms: TypeAlias = list[
    "aws_sdk_codebuild.types.environment_platform.EnvironmentPlatform"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentPlatforms) -> list:
    import aws_sdk_codebuild.types.environment_platform

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.environment_platform.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentPlatforms:
    import aws_sdk_codebuild.types.environment_platform

    out: EnvironmentPlatforms = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.environment_platform.deserialize_aws_json_1_1(item)
        )
    return out
