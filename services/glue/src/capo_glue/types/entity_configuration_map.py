"""Generated from Smithy shape ``com.amazonaws.glue#EntityConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.entity_configuration
    import capo_glue.types.entity_configuration_map_key_string

EntityConfigurationMap: TypeAlias = dict[
    "capo_glue.types.entity_configuration_map_key_string.EntityConfigurationMapKeyString",
    "capo_glue.types.entity_configuration.EntityConfiguration",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EntityConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.entity_configuration

        out[key] = capo_glue.types.entity_configuration.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityConfigurationMap:
    out: EntityConfigurationMap = {}
    for key, value in data.items():
        import capo_glue.types.entity_configuration

        out[key] = capo_glue.types.entity_configuration.deserialize_aws_json_1_1(value)
    return out
