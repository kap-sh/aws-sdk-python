"""Generated from Smithy shape ``com.amazonaws.sagemaker#SourceAlgorithmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.source_algorithm

SourceAlgorithmList: TypeAlias = list[
    "aws_sdk_sagemaker.types.source_algorithm.SourceAlgorithm"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAlgorithmList) -> list:
    import aws_sdk_sagemaker.types.source_algorithm

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.source_algorithm.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SourceAlgorithmList:
    import aws_sdk_sagemaker.types.source_algorithm

    out: SourceAlgorithmList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.source_algorithm.deserialize_aws_json_1_1(item)
        )
    return out
