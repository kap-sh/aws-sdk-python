"""Generated from Smithy shape ``com.amazonaws.bedrockagent#GetFlowAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_alias_identifier
    import aws_sdk_bedrock_agent.types.flow_identifier


class GetFlowAliasRequest(TypedDict):
    flow_identifier: "aws_sdk_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow that the alias belongs to.</p>"""
    alias_identifier: (
        "aws_sdk_bedrock_agent.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the alias for which to retrieve information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFlowAliasRequest:
    out: GetFlowAliasRequest = {}  # type: ignore[typeddict-item]
    return out
