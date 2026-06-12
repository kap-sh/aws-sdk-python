"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingInstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_instance_type

TrainingInstanceTypes: TypeAlias = list[
    "aws_sdk_sagemaker.types.training_instance_type.TrainingInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingInstanceTypes) -> list:
    import aws_sdk_sagemaker.types.training_instance_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.training_instance_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TrainingInstanceTypes:
    import aws_sdk_sagemaker.types.training_instance_type

    out: TrainingInstanceTypes = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.training_instance_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
