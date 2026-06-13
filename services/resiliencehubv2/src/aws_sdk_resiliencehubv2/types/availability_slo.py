"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AvailabilitySlo``."""

from typing import TypedDict

from typing_extensions import NotRequired


class AvailabilitySlo(TypedDict):
    target: NotRequired["float"]
    """<p>The target availability percentage, expressed as a value between 0 and 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilitySlo) -> dict:
    out: dict = {}
    if "target" in value:
        out["target"] = value["target"]
    return out


def deserialize_json(data: dict) -> AvailabilitySlo:
    out: AvailabilitySlo = {}  # type: ignore[typeddict-item]
    if "target" in data:
        out["target"] = data["target"]
    return out
