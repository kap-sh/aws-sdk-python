"""Generated from Smithy shape ``com.amazonaws.securityagent#CustomHeader``."""

from typing_extensions import NotRequired, TypedDict


class CustomHeader(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the custom header.</p>"""
    value: NotRequired["str"]
    """<p>The value of the custom header.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomHeader) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CustomHeader:
    out: CustomHeader = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
