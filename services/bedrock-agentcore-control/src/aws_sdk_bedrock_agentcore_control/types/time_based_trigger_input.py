"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TimeBasedTriggerInput``."""

from typing import TypedDict


class TimeBasedTriggerInput(TypedDict):
    idle_session_timeout: "int"
    """<p>Idle session timeout (seconds) that triggers memory processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeBasedTriggerInput) -> dict:
    out: dict = {}
    out["idleSessionTimeout"] = value.get("idle_session_timeout", 20)
    return out


def deserialize_json(data: dict) -> TimeBasedTriggerInput:
    out: TimeBasedTriggerInput = {}  # type: ignore[typeddict-item]
    if "idleSessionTimeout" in data:
        out["idle_session_timeout"] = data["idleSessionTimeout"]
    else:
        out["idle_session_timeout"] = 20
    return out
