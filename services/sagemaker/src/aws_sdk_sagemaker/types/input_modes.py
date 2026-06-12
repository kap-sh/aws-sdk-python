"""Generated from Smithy shape ``com.amazonaws.sagemaker#InputModes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.training_input_mode

InputModes: TypeAlias = list[
    "aws_sdk_sagemaker.types.training_input_mode.TrainingInputMode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputModes) -> list:
    import aws_sdk_sagemaker.types.training_input_mode

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.training_input_mode.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InputModes:
    import aws_sdk_sagemaker.types.training_input_mode

    out: InputModes = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.training_input_mode.deserialize_aws_json_1_1(item)
        )
    return out
