"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ConfidenceInterval``."""

from typing_extensions import NotRequired, TypedDict


class ConfidenceInterval(TypedDict, closed=True):
    lower: NotRequired["float"]
    """<p>The lower bound of the confidence interval.</p>"""
    upper: NotRequired["float"]
    """<p>The upper bound of the confidence interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfidenceInterval) -> dict:
    out: dict = {}
    if "lower" in value:
        out["lower"] = (
            "NaN"
            if value["lower"] != value["lower"]
            else "Infinity"
            if value["lower"] == float("inf")
            else "-Infinity"
            if value["lower"] == float("-inf")
            else value["lower"]
        )
    if "upper" in value:
        out["upper"] = (
            "NaN"
            if value["upper"] != value["upper"]
            else "Infinity"
            if value["upper"] == float("inf")
            else "-Infinity"
            if value["upper"] == float("-inf")
            else value["upper"]
        )
    return out


def deserialize_json(data: dict) -> ConfidenceInterval:
    out: ConfidenceInterval = {}  # type: ignore[typeddict-item]
    if data.get("lower") is not None:
        out["lower"] = float(data["lower"])
    if data.get("upper") is not None:
        out["upper"] = float(data["upper"])
    return out
