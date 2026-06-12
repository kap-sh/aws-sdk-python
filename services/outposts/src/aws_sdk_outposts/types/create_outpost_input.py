"""Generated from Smithy shape ``com.amazonaws.outposts#CreateOutpostInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.availability_zone
    import aws_sdk_outposts.types.availability_zone_id
    import aws_sdk_outposts.types.outpost_description
    import aws_sdk_outposts.types.outpost_name
    import aws_sdk_outposts.types.site_id
    import aws_sdk_outposts.types.supported_hardware_type
    import aws_sdk_outposts.types.tag_map


class CreateOutpostInput(TypedDict):
    name: "aws_sdk_outposts.types.outpost_name.OutpostName"
    description: NotRequired[
        "aws_sdk_outposts.types.outpost_description.OutpostDescription"
    ]
    site_id: "aws_sdk_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""
    availability_zone: NotRequired[
        "aws_sdk_outposts.types.availability_zone.AvailabilityZone"
    ]
    availability_zone_id: NotRequired[
        "aws_sdk_outposts.types.availability_zone_id.AvailabilityZoneId"
    ]
    tags: NotRequired["aws_sdk_outposts.types.tag_map.TagMap"]
    """<p>The tags to apply to the Outpost.</p>"""
    supported_hardware_type: NotRequired[
        "aws_sdk_outposts.types.supported_hardware_type.SupportedHardwareType"
    ]
    """<p> The type of hardware for this Outpost. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutpostInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["SiteId"] = value["site_id"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "tags" in value:
        import aws_sdk_outposts.types.tag_map

        out["Tags"] = aws_sdk_outposts.types.tag_map.serialize_json(value["tags"])
    if "supported_hardware_type" in value:
        import aws_sdk_outposts.types.supported_hardware_type

        out["SupportedHardwareType"] = (
            aws_sdk_outposts.types.supported_hardware_type.serialize_json(
                value["supported_hardware_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateOutpostInput:
    out: CreateOutpostInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateOutpostInput.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    else:
        raise DeserializationError("CreateOutpostInput.site_id required")
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "AvailabilityZoneId" in data:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if "Tags" in data:
        import aws_sdk_outposts.types.tag_map

        out["tags"] = aws_sdk_outposts.types.tag_map.deserialize_json(data["Tags"])
    if "SupportedHardwareType" in data:
        import aws_sdk_outposts.types.supported_hardware_type

        out["supported_hardware_type"] = (
            aws_sdk_outposts.types.supported_hardware_type.deserialize_json(
                data["SupportedHardwareType"]
            )
        )
    return out
