"""Generated from Smithy shape ``com.amazonaws.sagemaker#RuleParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.config_key
    import capo_sagemaker.types.config_value

RuleParameters: TypeAlias = dict[
    "capo_sagemaker.types.config_key.ConfigKey",
    "capo_sagemaker.types.config_value.ConfigValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RuleParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleParameters:
    out: RuleParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
