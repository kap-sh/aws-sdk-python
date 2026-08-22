"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NumberValidation``."""

from typing_extensions import NotRequired, TypedDict


class NumberValidation(TypedDict, closed=True):
    min_value: NotRequired["float"]
    """<p>Minimum allowed value.</p>"""
    max_value: NotRequired["float"]
    """<p>Maximum allowed value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberValidation) -> dict:
    out: dict = {}
    if "min_value" in value:
        out["minValue"] = (
            "NaN"
            if value["min_value"] != value["min_value"]
            else "Infinity"
            if value["min_value"] == float("inf")
            else "-Infinity"
            if value["min_value"] == float("-inf")
            else value["min_value"]
        )
    if "max_value" in value:
        out["maxValue"] = (
            "NaN"
            if value["max_value"] != value["max_value"]
            else "Infinity"
            if value["max_value"] == float("inf")
            else "-Infinity"
            if value["max_value"] == float("-inf")
            else value["max_value"]
        )
    return out


def deserialize_json(data: dict) -> NumberValidation:
    out: NumberValidation = {}  # type: ignore[typeddict-item]
    if data.get("minValue") is not None:
        out["min_value"] = float(data["minValue"])
    if data.get("maxValue") is not None:
        out["max_value"] = float(data["maxValue"])
    return out
