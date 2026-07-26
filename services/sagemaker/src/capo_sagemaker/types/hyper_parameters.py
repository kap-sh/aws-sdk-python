"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_key
    import capo_sagemaker.types.hyper_parameter_value

HyperParameters: TypeAlias = dict[
    "capo_sagemaker.types.hyper_parameter_key.HyperParameterKey",
    "capo_sagemaker.types.hyper_parameter_value.HyperParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: HyperParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameters:
    out: HyperParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
