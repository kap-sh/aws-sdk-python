"""Generated from Smithy shape ``com.amazonaws.codepipeline#InputArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.input_artifact

InputArtifactList: TypeAlias = list[
    "aws_sdk_codepipeline.types.input_artifact.InputArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputArtifactList) -> list:
    import aws_sdk_codepipeline.types.input_artifact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.input_artifact.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InputArtifactList:
    import aws_sdk_codepipeline.types.input_artifact

    out: InputArtifactList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.input_artifact.deserialize_aws_json_1_1(item)
        )
    return out
