"""Generated from Smithy shape ``com.amazonaws.devopsagent#DisassociateServiceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.association_id


class DisassociateServiceInput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    association_id: "capo_devops_agent.types.association_id.AssociationId"
    """<p>The unique identifier of the given association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateServiceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateServiceInput:
    out: DisassociateServiceInput = {}  # type: ignore[typeddict-item]
    return out
