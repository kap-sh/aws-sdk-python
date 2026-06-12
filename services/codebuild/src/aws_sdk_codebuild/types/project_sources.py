"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.project_source

ProjectSources: TypeAlias = list["aws_sdk_codebuild.types.project_source.ProjectSource"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSources) -> list:
    import aws_sdk_codebuild.types.project_source

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.project_source.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProjectSources:
    import aws_sdk_codebuild.types.project_source

    out: ProjectSources = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.project_source.deserialize_aws_json_1_1(item)
        )
    return out
