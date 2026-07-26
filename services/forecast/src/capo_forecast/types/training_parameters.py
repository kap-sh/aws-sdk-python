"""Generated from Smithy shape ``com.amazonaws.forecast#TrainingParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_forecast.types.parameter_key
    import capo_forecast.types.parameter_value

TrainingParameters: TypeAlias = dict[
    "capo_forecast.types.parameter_key.ParameterKey",
    "capo_forecast.types.parameter_value.ParameterValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: TrainingParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingParameters:
    out: TrainingParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
