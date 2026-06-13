"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetAssociationInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.agent_space_id
    import aws_sdk_devops_agent.types.association_id


class GetAssociationInput(TypedDict):
    agent_space_id: "aws_sdk_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    association_id: "aws_sdk_devops_agent.types.association_id.AssociationId"
    """<p>The unique identifier of the given association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAssociationInput:
    out: GetAssociationInput = {}  # type: ignore[typeddict-item]
    return out
