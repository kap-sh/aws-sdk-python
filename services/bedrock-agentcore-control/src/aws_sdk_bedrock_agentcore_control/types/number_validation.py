"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NumberValidation``."""

from typing import TypedDict

from typing_extensions import NotRequired


class NumberValidation(TypedDict):
    min_value: NotRequired["float"]
    """<p>Minimum allowed value.</p>"""
    max_value: NotRequired["float"]
    """<p>Maximum allowed value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumberValidation) -> dict:
    out: dict = {}
    if "min_value" in value:
        out["minValue"] = value["min_value"]
    if "max_value" in value:
        out["maxValue"] = value["max_value"]
    return out


def deserialize_json(data: dict) -> NumberValidation:
    out: NumberValidation = {}  # type: ignore[typeddict-item]
    if "minValue" in data:
        out["min_value"] = data["minValue"]
    if "maxValue" in data:
        out["max_value"] = data["maxValue"]
    return out
