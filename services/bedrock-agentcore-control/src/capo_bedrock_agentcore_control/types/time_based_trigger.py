"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TimeBasedTrigger``."""

from typing_extensions import NotRequired, TypedDict


class TimeBasedTrigger(TypedDict, closed=True):
    idle_session_timeout: NotRequired["int"]
    """<p>Idle session timeout (seconds) that triggers memory processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeBasedTrigger) -> dict:
    out: dict = {}
    if "idle_session_timeout" in value:
        out["idleSessionTimeout"] = value["idle_session_timeout"]
    return out


def deserialize_json(data: dict) -> TimeBasedTrigger:
    out: TimeBasedTrigger = {}  # type: ignore[typeddict-item]
    if data.get("idleSessionTimeout") is not None:
        out["idle_session_timeout"] = data["idleSessionTimeout"]
    return out
