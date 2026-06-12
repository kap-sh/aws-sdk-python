"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactRevisionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_revision

ArtifactRevisionList: TypeAlias = list[
    "aws_sdk_codepipeline.types.artifact_revision.ArtifactRevision"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactRevisionList) -> list:
    import aws_sdk_codepipeline.types.artifact_revision

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.artifact_revision.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ArtifactRevisionList:
    import aws_sdk_codepipeline.types.artifact_revision

    out: ArtifactRevisionList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.artifact_revision.deserialize_aws_json_1_1(item)
        )
    return out
