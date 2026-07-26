"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#EnvironmentVariablesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.environment_variable_key
    import capo_bedrock_agentcore_control.types.environment_variable_value

EnvironmentVariablesMap: TypeAlias = dict[
    "capo_bedrock_agentcore_control.types.environment_variable_key.EnvironmentVariableKey",
    "capo_bedrock_agentcore_control.types.environment_variable_value.EnvironmentVariableValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: EnvironmentVariablesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> EnvironmentVariablesMap:
    out: EnvironmentVariablesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
