"""Generated from Smithy shape ``com.amazonaws.mediaconnect#InterfaceRequest``."""

from typing import TypedDict

from typing_extensions import NotRequired


class InterfaceRequest(TypedDict):
    name: NotRequired["str"]
    """<p> The name of the VPC interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> InterfaceRequest:
    out: InterfaceRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
