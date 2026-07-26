"""Generated from Smithy shape ``com.amazonaws.securityagent#AgentSpaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_securityagent.types.agent_space_id


class AgentSpaceSummary(TypedDict, closed=True):
    agent_space_id: "capo_securityagent.types.agent_space_id.AgentSpaceId"
    """<p>The unique identifier of the agent space.</p>"""
    name: "str"
    """<p>The name of the agent space.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time the agent space was created, in UTC format.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time the agent space was last updated, in UTC format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSpaceSummary) -> dict:
    out: dict = {}
    out["agentSpaceId"] = value["agent_space_id"]
    out["name"] = value["name"]
    if "created_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["createdAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_securityagent.types._prelude.timestamp

        out["updatedAt"] = capo_securityagent.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> AgentSpaceSummary:
    out: AgentSpaceSummary = {}  # type: ignore[typeddict-item]
    if "agentSpaceId" in data:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("AgentSpaceSummary.agent_space_id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AgentSpaceSummary.name required")
    if "createdAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["created_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import capo_securityagent.types._prelude.timestamp

        out["updated_at"] = (
            capo_securityagent.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
