"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#SupportedResourceType``."""

from typing import TypedDict

from typing_extensions import NotRequired


class SupportedResourceType(TypedDict):
    service: NotRequired["str"]
    """<p>The Amazon Web Services service that is associated with the resource type. This is the primary service that lets you create and interact with resources of this type.</p>"""
    resource_type: NotRequired["str"]
    """<p>The unique identifier of the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SupportedResourceType) -> dict:
    out: dict = {}
    if "service" in value:
        out["Service"] = value["service"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> SupportedResourceType:
    out: SupportedResourceType = {}  # type: ignore[typeddict-item]
    if "Service" in data:
        out["service"] = data["Service"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out
