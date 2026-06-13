"""Generated from Smithy shape ``com.amazonaws.qconnect#Annotation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Annotation(TypedDict):
    title: NotRequired["str"]
    """<p>The title of the annotation.</p>"""
    destructive_hint: NotRequired["bool"]
    """<p>A hint indicating that the annotation contains potentially destructive content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Annotation) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "destructive_hint" in value:
        out["destructiveHint"] = value["destructive_hint"]
    return out


def deserialize_json(data: dict) -> Annotation:
    out: Annotation = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    if "destructiveHint" in data:
        out["destructive_hint"] = data["destructiveHint"]
    return out
