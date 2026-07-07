"""Generated from Smithy shape ``com.amazonaws.bedrockagent#LoopFlowNodeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_definition


class LoopFlowNodeConfiguration(TypedDict, closed=True):
    definition: "aws_sdk_bedrock_agent.types.flow_definition.FlowDefinition"
    """<p>The definition of the DoWhile loop nodes and connections between nodes in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoopFlowNodeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.flow_definition

    out["definition"] = aws_sdk_bedrock_agent.types.flow_definition.serialize_json(
        value["definition"]
    )
    return out


def deserialize_json(data: dict) -> LoopFlowNodeConfiguration:
    out: LoopFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        import aws_sdk_bedrock_agent.types.flow_definition

        out["definition"] = (
            aws_sdk_bedrock_agent.types.flow_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("LoopFlowNodeConfiguration.definition required")
    return out
