"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.actor_id
    import capo_bedrock_agentcore.types.session_id


class SessionSummary(TypedDict, closed=True):
    session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The unique identifier of the session.</p>"""
    actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId"
    """<p>The identifier of the actor associated with the session.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the session was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["actorId"] = value["actor_id"]
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("SessionSummary.session_id required")
    if "actorId" in data:
        out["actor_id"] = data["actorId"]
    else:
        raise DeserializationError("SessionSummary.actor_id required")
    if "createdAt" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("SessionSummary.created_at required")
    return out
