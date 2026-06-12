"""Generated from Smithy shape ``com.amazonaws.datazone#ConfigurableActionParameter``."""

from typing import TypedDict
from typing_extensions import NotRequired

class ConfigurableActionParameter(TypedDict):
    key: NotRequired["str"]
    """<p>The key of the configurable action parameter.</p>"""
    value: NotRequired["str"]
    """<p>The value of the configurable action parameter.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ConfigurableActionParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ConfigurableActionParameter:
    out: ConfigurableActionParameter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "value" in data:
        out["value"] = data["value"]
    return out