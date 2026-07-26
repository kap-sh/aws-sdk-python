"""Generated from Smithy shape ``com.amazonaws.mwaa#AirflowConfigurationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mwaa.types.config_key
    import capo_mwaa.types.config_value

AirflowConfigurationOptions: TypeAlias = dict[
    "capo_mwaa.types.config_key.ConfigKey", "capo_mwaa.types.config_value.ConfigValue"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AirflowConfigurationOptions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AirflowConfigurationOptions:
    out: AirflowConfigurationOptions = {}
    for key, value in data.items():
        out[key] = value
    return out
