"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MemorySessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.memory_id
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.summary_text


class MemorySessionSummary(TypedDict, closed=True):
    memory_id: NotRequired["capo_bedrock_agent_runtime.types.memory_id.MemoryId"]
    """<p>The unique identifier of the memory where the session summary is stored.</p>"""
    session_id: NotRequired["capo_bedrock_agent_runtime.types.session_id.SessionId"]
    """<p>The identifier for this session.</p>"""
    session_start_time: NotRequired[
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p>The start time for this session.</p>"""
    session_expiry_time: NotRequired[
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the memory duration for the session is set to end.</p>"""
    summary_text: NotRequired[
        "capo_bedrock_agent_runtime.types.summary_text.SummaryText"
    ]
    """<p>The summarized text for this session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemorySessionSummary) -> dict:
    out: dict = {}
    if "memory_id" in value:
        out["memoryId"] = value["memory_id"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "session_start_time" in value:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["sessionStartTime"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
                value["session_start_time"]
            )
        )
    if "session_expiry_time" in value:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["sessionExpiryTime"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
                value["session_expiry_time"]
            )
        )
    if "summary_text" in value:
        out["summaryText"] = value["summary_text"]
    return out


def deserialize_json(data: dict) -> MemorySessionSummary:
    out: MemorySessionSummary = {}  # type: ignore[typeddict-item]
    if "memoryId" in data:
        out["memory_id"] = data["memoryId"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "sessionStartTime" in data:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["session_start_time"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["sessionStartTime"]
            )
        )
    if "sessionExpiryTime" in data:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["session_expiry_time"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["sessionExpiryTime"]
            )
        )
    if "summaryText" in data:
        out["summary_text"] = data["summaryText"]
    return out
