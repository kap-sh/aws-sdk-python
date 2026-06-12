"""Generated from Smithy shape ``com.amazonaws.sagemaker#CollectionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.config_key
    import aws_sdk_sagemaker.types.config_value

CollectionParameters: TypeAlias = dict[
    "aws_sdk_sagemaker.types.config_key.ConfigKey",
    "aws_sdk_sagemaker.types.config_value.ConfigValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CollectionParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> CollectionParameters:
    out: CollectionParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
