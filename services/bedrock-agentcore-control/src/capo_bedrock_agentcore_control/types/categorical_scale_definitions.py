"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CategoricalScaleDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.categorical_scale_definition

CategoricalScaleDefinitions: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.categorical_scale_definition.CategoricalScaleDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoricalScaleDefinitions) -> list:
    import capo_bedrock_agentcore_control.types.categorical_scale_definition

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.categorical_scale_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CategoricalScaleDefinitions:
    import capo_bedrock_agentcore_control.types.categorical_scale_definition

    out: CategoricalScaleDefinitions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.categorical_scale_definition.deserialize_json(
                item
            )
        )
    return out
