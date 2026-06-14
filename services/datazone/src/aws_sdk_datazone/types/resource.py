"""Generated from Smithy shape ``com.amazonaws.datazone#Resource``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError


class Resource(TypedDict):
    provider: NotRequired["str"]
    """<p>The provider of a provisioned resource of this Amazon DataZone environment.</p>"""
    name: NotRequired["str"]
    """<p>The name of a provisioned resource of this Amazon DataZone environment.</p>"""
    value: "str"
    """<p>The value of a provisioned resource of this Amazon DataZone environment.</p>"""
    type: "str"
    """<p>The type of a provisioned resource of this Amazon DataZone environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "provider" in value:
        out["provider"] = value["provider"]
    if "name" in value:
        out["name"] = value["name"]
    out["value"] = value["value"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "provider" in data:
        out["provider"] = data["provider"]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("Resource.value required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("Resource.type required")
    return out
