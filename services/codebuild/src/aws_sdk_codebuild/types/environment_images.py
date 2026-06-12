"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.environment_image

EnvironmentImages: TypeAlias = list[
    "aws_sdk_codebuild.types.environment_image.EnvironmentImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentImages) -> list:
    import aws_sdk_codebuild.types.environment_image

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.environment_image.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentImages:
    import aws_sdk_codebuild.types.environment_image

    out: EnvironmentImages = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.environment_image.deserialize_aws_json_1_1(item)
        )
    return out
