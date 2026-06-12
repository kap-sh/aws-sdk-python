"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CustomOrchestrationTraceEvent``."""

from typing import TypedDict
from typing_extensions import NotRequired

class CustomOrchestrationTraceEvent(TypedDict):
    text: NotRequired["str"]
    """<p> The text that prompted the event at this step. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CustomOrchestrationTraceEvent) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> CustomOrchestrationTraceEvent:
    out: CustomOrchestrationTraceEvent = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    return out