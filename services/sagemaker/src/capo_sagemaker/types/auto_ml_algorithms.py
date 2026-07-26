"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLAlgorithms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.auto_ml_algorithm

AutoMLAlgorithms: TypeAlias = list[
    "capo_sagemaker.types.auto_ml_algorithm.AutoMLAlgorithm"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLAlgorithms) -> list:
    import capo_sagemaker.types.auto_ml_algorithm

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.auto_ml_algorithm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AutoMLAlgorithms:
    import capo_sagemaker.types.auto_ml_algorithm

    out: AutoMLAlgorithms = []
    for item in data:
        out.append(
            capo_sagemaker.types.auto_ml_algorithm.deserialize_aws_json_1_1(item)
        )
    return out
