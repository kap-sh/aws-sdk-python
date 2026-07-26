"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingInstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_instance_type

TrainingInstanceTypes: TypeAlias = list[
    "capo_sagemaker.types.training_instance_type.TrainingInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingInstanceTypes) -> list:
    import capo_sagemaker.types.training_instance_type

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.training_instance_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingInstanceTypes:
    import capo_sagemaker.types.training_instance_type

    out: TrainingInstanceTypes = []
    for item in data:
        out.append(
            capo_sagemaker.types.training_instance_type.deserialize_aws_json_1_1(item)
        )
    return out
