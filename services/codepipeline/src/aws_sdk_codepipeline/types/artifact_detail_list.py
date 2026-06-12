"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.artifact_detail

ArtifactDetailList: TypeAlias = list[
    "aws_sdk_codepipeline.types.artifact_detail.ArtifactDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ArtifactDetailList) -> list:
    import aws_sdk_codepipeline.types.artifact_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.artifact_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ArtifactDetailList:
    import aws_sdk_codepipeline.types.artifact_detail

    out: ArtifactDetailList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.artifact_detail.deserialize_aws_json_1_1(item)
        )
    return out
