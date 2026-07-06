"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#ResourceSummary``."""

from typing_extensions import NotRequired, TypedDict

from aws_sdk_snow_device_management.errors import DeserializationError


class ResourceSummary(TypedDict, closed=True):
    resource_type: "str"
    """<p>The resource type.</p>"""
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    id: NotRequired["str"]
    """<p>The ID of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSummary) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> ResourceSummary:
    out: ResourceSummary = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ResourceSummary.resource_type required")
    if "arn" in data:
        out["arn"] = data["arn"]
    if "id" in data:
        out["id"] = data["id"]
    return out
