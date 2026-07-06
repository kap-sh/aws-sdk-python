"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ApiParameter``."""

from typing_extensions import NotRequired, TypedDict


class ApiParameter(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the parameter.</p>"""
    type: NotRequired["str"]
    """<p>The data type for the parameter.</p>"""
    value: NotRequired["str"]
    """<p>The value of the parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApiParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        out["type"] = value["type"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ApiParameter:
    out: ApiParameter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        out["type"] = data["type"]
    if "value" in data:
        out["value"] = data["value"]
    return out
