"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_condition

FlowConditions: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.flow_condition.FlowCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: FlowConditions) -> list:
    import aws_sdk_bedrock_agent.types.flow_condition

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agent.types.flow_condition.serialize_json(item))
    return out


def deserialize_json(data: list) -> FlowConditions:
    import aws_sdk_bedrock_agent.types.flow_condition

    out: FlowConditions = []
    for item in data:
        out.append(aws_sdk_bedrock_agent.types.flow_condition.deserialize_json(item))
    return out
