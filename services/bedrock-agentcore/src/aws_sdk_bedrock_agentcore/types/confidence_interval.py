"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ConfidenceInterval``."""

from typing import TypedDict
from typing_extensions import NotRequired

class ConfidenceInterval(TypedDict):
    lower: NotRequired["float"]
    """<p>The lower bound of the confidence interval.</p>"""
    upper: NotRequired["float"]
    """<p>The upper bound of the confidence interval.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConfidenceInterval) -> dict:
    out: dict = {}
    if "lower" in value:
        out["lower"] = value["lower"]
    if "upper" in value:
        out["upper"] = value["upper"]
    return out


def deserialize_json(data: dict) -> ConfidenceInterval:
    out: ConfidenceInterval = {}  # type: ignore[typeddict-item]
    if "lower" in data:
        out["lower"] = data["lower"]
    if "upper" in data:
        out["upper"] = data["upper"]
    return out