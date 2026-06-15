"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NumericalScaleDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.numerical_scale_definition

NumericalScaleDefinitions: TypeAlias = list[
    "aws_sdk_bedrock_agentcore_control.types.numerical_scale_definition.NumericalScaleDefinition"
]


# --- restJson1 ser/de ---
def serialize_json(value: NumericalScaleDefinitions) -> list:
    import aws_sdk_bedrock_agentcore_control.types.numerical_scale_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.numerical_scale_definition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> NumericalScaleDefinitions:
    import aws_sdk_bedrock_agentcore_control.types.numerical_scale_definition

    out: NumericalScaleDefinitions = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore_control.types.numerical_scale_definition.deserialize_json(
                item
            )
        )
    return out
