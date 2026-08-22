"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SchemaProperties``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.schema_definition

SchemaProperties: TypeAlias = dict[
    "str", "capo_bedrock_agentcore_control.types.schema_definition.SchemaDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SchemaProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock_agentcore_control.types.schema_definition

        out[key] = (
            capo_bedrock_agentcore_control.types.schema_definition.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> SchemaProperties:
    out: SchemaProperties = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_bedrock_agentcore_control.types.schema_definition

        out[key] = (
            capo_bedrock_agentcore_control.types.schema_definition.deserialize_json(
                value
            )
        )
    return out
