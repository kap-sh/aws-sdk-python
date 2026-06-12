"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowValidations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_validation

FlowValidations: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.flow_validation.FlowValidation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowValidations) -> list:
    import aws_sdk_bedrock_agent.types.flow_validation

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.flow_validation.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowValidations:
    import aws_sdk_bedrock_agent.types.flow_validation

    out: FlowValidations = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.flow_validation.deserialize_json(item))
    return out
