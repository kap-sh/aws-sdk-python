"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ConfigurationsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.configuration
    import aws_sdk_accessanalyzer.types.configurations_map_key

ConfigurationsMap: TypeAlias = dict[
    "aws_sdk_accessanalyzer.types.configurations_map_key.ConfigurationsMapKey",
    "aws_sdk_accessanalyzer.types.configuration.Configuration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConfigurationsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_accessanalyzer.types.configuration

        out[key] = aws_sdk_accessanalyzer.types.configuration.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ConfigurationsMap:
    out: ConfigurationsMap = {}
    for key, value in data.items():
        import aws_sdk_accessanalyzer.types.configuration

        out[key] = aws_sdk_accessanalyzer.types.configuration.deserialize_json(value)
    return out
