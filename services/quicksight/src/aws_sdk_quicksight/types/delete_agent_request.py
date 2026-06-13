"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteAgentRequest``."""

from typing import TypedDict


class DeleteAgentRequest(TypedDict):
    agent_id: "str"
    """<p>The unique identifier for the agent to delete.</p>"""
    aws_account_id: "str"
    """<p>The ID of the Amazon Web Services account that contains the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAgentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAgentRequest:
    out: DeleteAgentRequest = {}  # type: ignore[typeddict-item]
    return out
