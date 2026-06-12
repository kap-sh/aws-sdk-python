"""Generated from Smithy shape ``com.amazonaws.codebuild#ResolvedSecondaryArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.resolved_artifact

ResolvedSecondaryArtifacts: TypeAlias = list[
    "aws_sdk_codebuild.types.resolved_artifact.ResolvedArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolvedSecondaryArtifacts) -> list:
    import aws_sdk_codebuild.types.resolved_artifact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.resolved_artifact.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResolvedSecondaryArtifacts:
    import aws_sdk_codebuild.types.resolved_artifact

    out: ResolvedSecondaryArtifacts = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.resolved_artifact.deserialize_aws_json_1_1(item)
        )
    return out
