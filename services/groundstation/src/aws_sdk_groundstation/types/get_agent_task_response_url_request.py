"""Generated from Smithy shape ``com.amazonaws.groundstation#GetAgentTaskResponseUrlRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class GetAgentTaskResponseUrlRequest(TypedDict):
    agent_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>UUID of agent requesting the response URL.</p>"""
    task_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>GUID of the agent task for which the response URL is being requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentTaskResponseUrlRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentTaskResponseUrlRequest:
    out: GetAgentTaskResponseUrlRequest = {}  # type: ignore[typeddict-item]
    return out
