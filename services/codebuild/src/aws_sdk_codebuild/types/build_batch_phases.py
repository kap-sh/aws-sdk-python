"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatchPhases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_batch_phase

BuildBatchPhases: TypeAlias = list[
    "aws_sdk_codebuild.types.build_batch_phase.BuildBatchPhase"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildBatchPhases) -> list:
    import aws_sdk_codebuild.types.build_batch_phase

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codebuild.types.build_batch_phase.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BuildBatchPhases:
    import aws_sdk_codebuild.types.build_batch_phase

    out: BuildBatchPhases = []
    for item in data:
        out.append(
            aws_sdk_codebuild.types.build_batch_phase.deserialize_aws_json_1_1(item)
        )
    return out
