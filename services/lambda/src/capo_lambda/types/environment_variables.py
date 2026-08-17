"""Generated from Smithy shape ``com.amazonaws.lambda#EnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.environment_variable_name
    import capo_lambda.types.environment_variable_value

EnvironmentVariables: TypeAlias = dict[
    "capo_lambda.types.environment_variable_name.EnvironmentVariableName",
    "capo_lambda.types.environment_variable_value.EnvironmentVariableValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EnvironmentVariables) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EnvironmentVariables:
    out: EnvironmentVariables = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
