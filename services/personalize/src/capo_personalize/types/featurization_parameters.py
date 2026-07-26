"""Generated from Smithy shape ``com.amazonaws.personalize#FeaturizationParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.parameter_name
    import capo_personalize.types.parameter_value

FeaturizationParameters: TypeAlias = dict[
    "capo_personalize.types.parameter_name.ParameterName",
    "capo_personalize.types.parameter_value.ParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FeaturizationParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> FeaturizationParameters:
    out: FeaturizationParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
