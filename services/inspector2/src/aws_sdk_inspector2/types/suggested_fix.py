"""Generated from Smithy shape ``com.amazonaws.inspector2#SuggestedFix``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SuggestedFix(TypedDict):
    description: NotRequired["str"]
    """<p>The fix's description.</p>"""
    code: NotRequired["str"]
    """<p>The fix's code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedFix) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "code" in value:
        out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> SuggestedFix:
    out: SuggestedFix = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "code" in data:
        out["code"] = data["code"]
    return out
