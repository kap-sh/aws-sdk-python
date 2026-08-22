"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Parameter``."""

from typing_extensions import NotRequired, TypedDict


class Parameter(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the parameter.</p>"""
    type: NotRequired["str"]
    """<p>The type of the parameter.</p>"""
    value: NotRequired["str"]
    """<p>The value of the parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Parameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Parameter:
    out: Parameter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("value") is not None:
        out["value"] = data["value"]
    return out
