"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLAlgorithms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_ml_algorithm

AutoMLAlgorithms: TypeAlias = list[
    "aws_sdk_sagemaker.types.auto_ml_algorithm.AutoMLAlgorithm"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLAlgorithms) -> list:
    import aws_sdk_sagemaker.types.auto_ml_algorithm

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_algorithm.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLAlgorithms:
    import aws_sdk_sagemaker.types.auto_ml_algorithm

    out: AutoMLAlgorithms = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.auto_ml_algorithm.deserialize_aws_json_1_1(item)
        )
    return out
