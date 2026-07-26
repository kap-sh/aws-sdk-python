"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteFlowAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_alias_identifier
    import capo_bedrock_agent.types.flow_identifier


class DeleteFlowAliasRequest(TypedDict, closed=True):
    flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow that the alias belongs to.</p>"""
    alias_identifier: (
        "capo_bedrock_agent.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the alias to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFlowAliasRequest:
    out: DeleteFlowAliasRequest = {}  # type: ignore[typeddict-item]
    return out
