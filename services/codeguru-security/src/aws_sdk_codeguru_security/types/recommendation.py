"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#Recommendation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Recommendation(TypedDict):
    text: NotRequired["str"]
    """<p>The recommended course of action to remediate the finding.</p>"""
    url: NotRequired["str"]
    """<p>The URL address to the recommendation for remediating the finding. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Recommendation) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> Recommendation:
    out: Recommendation = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    if "url" in data:
        out["url"] = data["url"]
    return out
