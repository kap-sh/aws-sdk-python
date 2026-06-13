"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Interface``."""

from typing import TypedDict

from typing_extensions import NotRequired


class Interface(TypedDict):
    name: NotRequired["str"]
    """<p> The name of the VPC interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Interface) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> Interface:
    out: Interface = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
