"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ConfigurationsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.configuration
    import capo_accessanalyzer.types.configurations_map_key

ConfigurationsMap: TypeAlias = dict[
    "capo_accessanalyzer.types.configurations_map_key.ConfigurationsMapKey",
    "capo_accessanalyzer.types.configuration.Configuration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConfigurationsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_accessanalyzer.types.configuration

        out[key] = capo_accessanalyzer.types.configuration.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ConfigurationsMap:
    out: ConfigurationsMap = {}
    for key, value in data.items():
        import capo_accessanalyzer.types.configuration

        out[key] = capo_accessanalyzer.types.configuration.deserialize_json(value)
    return out
