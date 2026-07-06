"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SessionSummaryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.max_recent_sessions


class SessionSummaryConfiguration(TypedDict, closed=True):
    max_recent_sessions: NotRequired[
        "aws_sdk_bedrock_agent.types.max_recent_sessions.MaxRecentSessions"
    ]
    """<p>Maximum number of recent session summaries to include in the agent's prompt context.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummaryConfiguration) -> dict:
    out: dict = {}
    if "max_recent_sessions" in value:
        out["maxRecentSessions"] = value["max_recent_sessions"]
    return out


def deserialize_json(data: dict) -> SessionSummaryConfiguration:
    out: SessionSummaryConfiguration = {}  # type: ignore[typeddict-item]
    if "maxRecentSessions" in data:
        out["max_recent_sessions"] = data["maxRecentSessions"]
    return out
