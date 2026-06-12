"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.build_batch

BuildBatches: TypeAlias = list["aws_sdk_codebuild.types.build_batch.BuildBatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildBatches) -> list:
    import aws_sdk_codebuild.types.build_batch

    out: list = []
    for item in value:
        out.append(aws_sdk_codebuild.types.build_batch.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildBatches:
    import aws_sdk_codebuild.types.build_batch

    out: BuildBatches = []
    for item in data:
        out.append(aws_sdk_codebuild.types.build_batch.deserialize_aws_json_1_1(item))
    return out
