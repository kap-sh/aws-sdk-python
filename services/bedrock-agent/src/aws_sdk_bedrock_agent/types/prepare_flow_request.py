"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PrepareFlowRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_identifier


class PrepareFlowRequest(TypedDict):
    flow_identifier: "aws_sdk_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrepareFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PrepareFlowRequest:
    out: PrepareFlowRequest = {}  # type: ignore[typeddict-item]
    return out
