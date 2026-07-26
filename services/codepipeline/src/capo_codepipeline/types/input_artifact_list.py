"""Generated from Smithy shape ``com.amazonaws.codepipeline#InputArtifactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.input_artifact

InputArtifactList: TypeAlias = list[
    "capo_codepipeline.types.input_artifact.InputArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputArtifactList) -> list:
    import capo_codepipeline.types.input_artifact

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.input_artifact.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InputArtifactList:
    import capo_codepipeline.types.input_artifact

    out: InputArtifactList = []
    for item in data:
        out.append(
            capo_codepipeline.types.input_artifact.deserialize_aws_json_1_1(item)
        )
    return out
