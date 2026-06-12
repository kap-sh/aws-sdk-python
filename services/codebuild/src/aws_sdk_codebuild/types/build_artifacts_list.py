"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildArtifactsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_artifacts

BuildArtifactsList: TypeAlias = list[
    "aws_sdk_codebuild.types.build_artifacts.BuildArtifacts"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildArtifactsList) -> list:
    import aws_sdk_codebuild.types.build_artifacts

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.build_artifacts.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildArtifactsList:
    import aws_sdk_codebuild.types.build_artifacts

    out: BuildArtifactsList = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.build_artifacts.deserialize_aws_json_1_1(item)
        )
    return out
