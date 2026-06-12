"""Generated from Smithy shape ``com.amazonaws.codebuild#Builds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build

Builds: TypeAlias = list["aws_sdk_codebuild.types.build.Build"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Builds) -> list:
    import aws_sdk_codebuild.types.build

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.build.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Builds:
    import aws_sdk_codebuild.types.build

    out: Builds = []
    for item in data:
        out.append(aws_sdk_codebuild.types.build.deserialize_aws_json_1_1(item))
    return out
