"""Generated from Smithy shape ``com.amazonaws.sagemaker#InputModes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.training_input_mode

InputModes: TypeAlias = list[
    "capo_sagemaker.types.training_input_mode.TrainingInputMode"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputModes) -> list:
    import capo_sagemaker.types.training_input_mode

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.training_input_mode.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InputModes:
    import capo_sagemaker.types.training_input_mode

    out: InputModes = []
    for item in data:
        out.append(
            capo_sagemaker.types.training_input_mode.deserialize_aws_json_1_1(item)
        )
    return out
