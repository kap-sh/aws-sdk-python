"""Generated from Smithy shape ``com.amazonaws.tnb#ToscaOverride``."""

from typing_extensions import NotRequired, TypedDict


class ToscaOverride(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>Name of the TOSCA override.</p>"""
    default_value: NotRequired["str"]
    """<p>Default value for the override.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToscaOverride) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> ToscaOverride:
    out: ToscaOverride = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    return out
