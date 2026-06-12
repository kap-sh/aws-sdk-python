"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetFlowVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_identifier
    import aws_sdk_bedrock_agent.types.numerical_version


class GetFlowVersionRequest(TypedDict):
    flow_identifier: "aws_sdk_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow for which to get information.</p>"""
    flow_version: "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version of the flow for which to get information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFlowVersionRequest:
    out: GetFlowVersionRequest = {}  # type: ignore[typeddict-item]
    return out
