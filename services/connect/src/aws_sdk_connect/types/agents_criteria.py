"""Generated from Smithy shape ``com.amazonaws.connect#AgentsCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_ids


class AgentsCriteria(TypedDict, closed=True):
    agent_ids: NotRequired["aws_sdk_connect.types.agent_ids.AgentIds"]
    """<p>An object to specify a list of agents, by user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentsCriteria) -> dict:
    out: dict = {}
    if "agent_ids" in value:
        import aws_sdk_connect.types.agent_ids

        out["AgentIds"] = aws_sdk_connect.types.agent_ids.serialize_json(
            value["agent_ids"]
        )
    return out


def deserialize_json(data: dict) -> AgentsCriteria:
    out: AgentsCriteria = {}  # type: ignore[typeddict-item]
    if "AgentIds" in data:
        import aws_sdk_connect.types.agent_ids

        out["agent_ids"] = aws_sdk_connect.types.agent_ids.deserialize_json(
            data["AgentIds"]
        )
    return out
