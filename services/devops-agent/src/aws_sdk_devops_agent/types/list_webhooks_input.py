"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListWebhooksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.association_id


class ListWebhooksInput(TypedDict, closed=True):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    association_id: "aws_sdk_devops_agent.types.association_id.AssociationId"
    """<p>The unique identifier of the given association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWebhooksInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListWebhooksInput:
    out: ListWebhooksInput = {}  # type: ignore[typeddict-item]
    return out
