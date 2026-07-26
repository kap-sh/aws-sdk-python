"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ActorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.actor_id


class ActorSummary(TypedDict, closed=True):
    actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The unique identifier of the actor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActorSummary) -> dict:
    out: dict = {}
    out["actorId"] = value["actor_id"]
    return out


def deserialize_json(data: dict) -> ActorSummary:
    out: ActorSummary = {}  # type: ignore[typeddict-item]
    if "actorId" in data:
        out["actor_id"] = data["actorId"]
    else:
        raise DeserializationError("ActorSummary.actor_id required")
    return out
