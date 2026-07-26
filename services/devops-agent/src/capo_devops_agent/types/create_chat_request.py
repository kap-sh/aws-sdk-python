"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreateChatRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.resource_id
    import capo_devops_agent.types.user_type


class CreateChatRequest(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    user_id: NotRequired["capo_devops_agent.types.resource_id.ResourceId"]
    """<p>The user identifier for the chat. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>"""
    user_type: NotRequired["capo_devops_agent.types.user_type.UserType"]
    """<p>The authentication type of the user</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateChatRequest:
    out: CreateChatRequest = {}  # type: ignore[typeddict-item]
    return out
