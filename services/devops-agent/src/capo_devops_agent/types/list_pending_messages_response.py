"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListPendingMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.pending_messages


class ListPendingMessagesResponse(TypedDict, closed=True):
    agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId"
    execution_id: "str"
    """<p>The unique identifier for the execution.</p>"""
    messages: "capo_devops_agent.types.pending_messages.PendingMessages"
    """<p>The list of pending messages for the execution.</p>"""
    created_at: "datetime.datetime"
    """<p>Timestamp when the pending messages were created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPendingMessagesResponse) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["executionId"] = value["execution_id"]
    import capo_devops_agent.types.pending_messages

    out["messages"] = capo_devops_agent.types.pending_messages.serialize_json(
        value.get("messages", [])
    )
    import capo_devops_agent.types._prelude.timestamp

    out["createdAt"] = capo_devops_agent.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> ListPendingMessagesResponse:
    out: ListPendingMessagesResponse = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError(
            "ListPendingMessagesResponse.agent_space_id required"
        )
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    else:
        raise DeserializationError("ListPendingMessagesResponse.execution_id required")
    if "messages" in data:
        import capo_devops_agent.types.pending_messages

        out["messages"] = capo_devops_agent.types.pending_messages.deserialize_json(
            data["messages"]
        )
    else:
        out["messages"] = []
    if "createdAt" in data:
        import capo_devops_agent.types._prelude.timestamp

        out["created_at"] = capo_devops_agent.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ListPendingMessagesResponse.created_at required")
    return out
