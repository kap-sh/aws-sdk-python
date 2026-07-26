"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#Tool``."""

from typing_extensions import NotRequired, TypedDict


class Tool(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of an AWS service. </p>"""
    url: NotRequired["str"]
    """<p>The URL of an AWS service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Tool) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> Tool:
    out: Tool = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "url" in data:
        out["url"] = data["url"]
    return out
