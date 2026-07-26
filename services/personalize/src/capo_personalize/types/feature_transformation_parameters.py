"""Generated from Smithy shape ``com.amazonaws.personalize#FeatureTransformationParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.parameter_name
    import capo_personalize.types.parameter_value

FeatureTransformationParameters: TypeAlias = dict[
    "capo_personalize.types.parameter_name.ParameterName",
    "capo_personalize.types.parameter_value.ParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FeatureTransformationParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureTransformationParameters:
    out: FeatureTransformationParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
