"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConditionFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_conditions


class ConditionFlowNodeConfiguration(TypedDict):
    conditions: "aws_sdk_bedrock_agent.types.flow_conditions.FlowConditions"
    """<p>An array of conditions. Each member contains the name of a condition and an expression that defines the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionFlowNodeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.flow_conditions

    out["conditions"] = aws_sdk_bedrock_agent.types.flow_conditions.serialize_json(
        value["conditions"]
    )
    return out


def deserialize_json(data: dict) -> ConditionFlowNodeConfiguration:
    out: ConditionFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if "conditions" in data:
        import aws_sdk_bedrock_agent.types.flow_conditions

        out["conditions"] = (
            aws_sdk_bedrock_agent.types.flow_conditions.deserialize_json(
                data["conditions"]
            )
        )
    else:
        raise DeserializationError("ConditionFlowNodeConfiguration.conditions required")
    return out
