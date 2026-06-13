"""Generated from Smithy shape ``com.amazonaws.rtbfabric#HeaderTagAction``."""

from typing import TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError


class HeaderTagAction(TypedDict):
    name: "str"
    """<p>The name of the bid action.</p>"""
    value: "str"
    """<p>The value of the bid action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HeaderTagAction) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> HeaderTagAction:
    out: HeaderTagAction = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("HeaderTagAction.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("HeaderTagAction.value required")
    return out
