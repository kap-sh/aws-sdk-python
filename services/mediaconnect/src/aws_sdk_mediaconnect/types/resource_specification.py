"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ResourceSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.resource_type


class ResourceSpecification(TypedDict):
    reserved_bitrate: NotRequired["int"]
    """<p> The amount of outbound bandwidth that is discounted in the offering.</p>"""
    resource_type: NotRequired["aws_sdk_mediaconnect.types.resource_type.ResourceType"]
    """<p> The type of resource and the unit that is being billed for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSpecification) -> dict:
    out: dict = {}
    if "reserved_bitrate" in value:
        out["reservedBitrate"] = value["reserved_bitrate"]
    if "resource_type" in value:
        import aws_sdk_mediaconnect.types.resource_type

        out["resourceType"] = aws_sdk_mediaconnect.types.resource_type.serialize_json(
            value["resource_type"]
        )
    return out


def deserialize_json(data: dict) -> ResourceSpecification:
    out: ResourceSpecification = {}  # type: ignore[typeddict-item]
    if "reservedBitrate" in data:
        out["reserved_bitrate"] = data["reservedBitrate"]
    if "resourceType" in data:
        import aws_sdk_mediaconnect.types.resource_type

        out["resource_type"] = (
            aws_sdk_mediaconnect.types.resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    return out
