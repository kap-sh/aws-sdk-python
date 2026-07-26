"""Generated from Smithy shape ``com.amazonaws.sagemaker#HookParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.config_key
    import capo_sagemaker.types.config_value

HookParameters: TypeAlias = dict[
    "capo_sagemaker.types.config_key.ConfigKey",
    "capo_sagemaker.types.config_value.ConfigValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: HookParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> HookParameters:
    out: HookParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
