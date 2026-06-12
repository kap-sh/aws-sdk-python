"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact

ArtifactList: TypeAlias = list["aws_sdk_codepipeline.types.artifact.Artifact"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactList) -> list:
    import aws_sdk_codepipeline.types.artifact

    out: list = []
    for item in value:
        out.append(aws_sdk_codepipeline.types.artifact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ArtifactList:
    import aws_sdk_codepipeline.types.artifact

    out: ArtifactList = []
    for item in data:
        out.append(aws_sdk_codepipeline.types.artifact.deserialize_aws_json_1_1(item))
    return out
