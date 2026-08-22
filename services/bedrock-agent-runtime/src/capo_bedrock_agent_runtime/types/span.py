"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Span``."""

from typing_extensions import NotRequired, TypedDict


class Span(TypedDict, closed=True):
    start: NotRequired["int"]
    """<p>Where the text with a citation starts in the generated output.</p>"""
    end: NotRequired["int"]
    """<p>Where the text with a citation ends in the generated output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Span) -> dict:
    out: dict = {}
    if "start" in value:
        out["start"] = value["start"]
    if "end" in value:
        out["end"] = value["end"]
    return out


def deserialize_json(data: dict) -> Span:
    out: Span = {}  # type: ignore[typeddict-item]
    if data.get("start") is not None:
        out["start"] = data["start"]
    if data.get("end") is not None:
        out["end"] = data["end"]
    return out
