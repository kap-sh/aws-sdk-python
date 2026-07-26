"""Generated from Smithy shape ``com.amazonaws.amplify#EnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.env_key
    import capo_amplify.types.env_value

EnvironmentVariables: TypeAlias = dict[
    "capo_amplify.types.env_key.EnvKey", "capo_amplify.types.env_value.EnvValue"
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
        out[key] = value
    return out
