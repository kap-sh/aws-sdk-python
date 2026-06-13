"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AnalyzePromptEvent``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AnalyzePromptEvent(TypedDict):
    message: NotRequired["str"]
    """<p>A message describing the analysis of the prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzePromptEvent) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AnalyzePromptEvent:
    out: AnalyzePromptEvent = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
