"""Generated from Smithy shape ``com.amazonaws.groundstation#GetAgentTaskResponseUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.uuid


class GetAgentTaskResponseUrlRequest(TypedDict, closed=True):
    agent_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of agent requesting the response URL.</p>"""
    task_id: "capo_groundstation.types.uuid.Uuid"
    """<p>GUID of the agent task for which the response URL is being requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentTaskResponseUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentTaskResponseUrlRequest:
    out: GetAgentTaskResponseUrlRequest = {}  # type: ignore[typeddict-item]
    return out
