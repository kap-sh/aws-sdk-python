"""Generated from Smithy shape ``com.amazonaws.sagemaker#TextGenerationHyperParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.text_generation_hyper_parameter_key
    import aws_sdk_sagemaker.types.text_generation_hyper_parameter_value

TextGenerationHyperParameters: TypeAlias = dict[
    "aws_sdk_sagemaker.types.text_generation_hyper_parameter_key.TextGenerationHyperParameterKey",
    "aws_sdk_sagemaker.types.text_generation_hyper_parameter_value.TextGenerationHyperParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TextGenerationHyperParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TextGenerationHyperParameters:
    out: TextGenerationHyperParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
