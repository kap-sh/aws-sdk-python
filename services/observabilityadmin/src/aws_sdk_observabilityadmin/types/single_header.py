"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#SingleHeader``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SingleHeader(TypedDict):
    name: NotRequired["str"]
    """<p> The name value, limited to 64 characters. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleHeader) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SingleHeader:
    out: SingleHeader = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
