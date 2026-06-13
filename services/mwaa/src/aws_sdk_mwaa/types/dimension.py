"""Generated from Smithy shape ``com.amazonaws.mwaa#Dimension``."""

from typing import TypedDict

from aws_sdk_mwaa.errors import DeserializationError


class Dimension(TypedDict):
    name: "str"
    """<p> <b>Internal only</b>. The name of the dimension.</p>"""
    value: "str"
    """<p> <b>Internal only</b>. The value of the dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Dimension.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Dimension.value required")
    return out
