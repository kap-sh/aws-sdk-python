"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProcessingEnvironmentMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.processing_environment_key
    import capo_sagemaker.types.processing_environment_value

ProcessingEnvironmentMap: TypeAlias = dict[
    "capo_sagemaker.types.processing_environment_key.ProcessingEnvironmentKey",
    "capo_sagemaker.types.processing_environment_value.ProcessingEnvironmentValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ProcessingEnvironmentMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ProcessingEnvironmentMap:
    out: ProcessingEnvironmentMap = {}
    for key, value in data.items():
        out[key] = value
    return out
