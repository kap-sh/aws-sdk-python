"""Generated from Smithy shape ``com.amazonaws.sagemaker#SourceAlgorithmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.source_algorithm

SourceAlgorithmList: TypeAlias = list[
    "capo_sagemaker.types.source_algorithm.SourceAlgorithm"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAlgorithmList) -> list:
    import capo_sagemaker.types.source_algorithm

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.source_algorithm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SourceAlgorithmList:
    import capo_sagemaker.types.source_algorithm

    out: SourceAlgorithmList = []
    for item in data:
        out.append(capo_sagemaker.types.source_algorithm.deserialize_aws_json_1_1(item))
    return out
