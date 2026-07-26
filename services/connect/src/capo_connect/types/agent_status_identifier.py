"""Generated from Smithy shape ``com.amazonaws.connect#AgentStatusIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_status_id
    import capo_connect.types.arn


class AgentStatusIdentifier(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the agent status.</p>"""
    id: NotRequired["capo_connect.types.agent_status_id.AgentStatusId"]
    """<p>The identifier of the agent status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentStatusIdentifier) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> AgentStatusIdentifier:
    out: AgentStatusIdentifier = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    return out
