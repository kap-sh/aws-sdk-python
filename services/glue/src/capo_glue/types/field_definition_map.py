"""Generated from Smithy shape ``com.amazonaws.glue#FieldDefinitionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.field_definition
    import capo_glue.types.field_definition_map_key_string

FieldDefinitionMap: TypeAlias = dict[
    "capo_glue.types.field_definition_map_key_string.FieldDefinitionMapKeyString",
    "capo_glue.types.field_definition.FieldDefinition",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FieldDefinitionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_glue.types.field_definition

        out[key] = capo_glue.types.field_definition.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldDefinitionMap:
    out: FieldDefinitionMap = {}
    for key, value in data.items():
        import capo_glue.types.field_definition

        out[key] = capo_glue.types.field_definition.deserialize_aws_json_1_1(value)
    return out
