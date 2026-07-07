"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_identifier


class GetFlowRequest(TypedDict, closed=True):
    flow_identifier: "aws_sdk_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFlowRequest:
    out: GetFlowRequest = {}  # type: ignore[typeddict-item]
    return out
