"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateAgentSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.agent_space_name
    import capo_devops_agent.types.description
    import capo_devops_agent.types.locale


class UpdateAgentSpaceInput(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the AgentSpace</p>"""
    name: NotRequired["capo_devops_agent.types.agent_space_name.AgentSpaceName"]
    """<p>The updated name of the AgentSpace.</p>"""
    description: NotRequired["capo_devops_agent.types.description.Description"]
    """<p>The updated description of the AgentSpace.</p>"""
    locale: NotRequired["capo_devops_agent.types.locale.Locale"]
    """<p>The updated locale for the AgentSpace, which determines the language used in agent responses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentSpaceInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_json(data: dict) -> UpdateAgentSpaceInput:
    out: UpdateAgentSpaceInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "locale" in data:
        out["locale"] = data["locale"]
    return out
