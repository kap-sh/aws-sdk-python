"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectArtifactsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.project_artifacts

ProjectArtifactsList: TypeAlias = list[
    "aws_sdk_codebuild.types.project_artifacts.ProjectArtifacts"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectArtifactsList) -> list:
    import aws_sdk_codebuild.types.project_artifacts

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.project_artifacts.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectArtifactsList:
    import aws_sdk_codebuild.types.project_artifacts

    out: ProjectArtifactsList = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.project_artifacts.deserialize_aws_json_1_1(item)
        )
    return out
