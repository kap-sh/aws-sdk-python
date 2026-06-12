"""Generated from Smithy shape ``com.amazonaws.outposts#Outpost``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.availability_zone
    import aws_sdk_outposts.types.availability_zone_id
    import aws_sdk_outposts.types.life_cycle_status
    import aws_sdk_outposts.types.outpost_arn
    import aws_sdk_outposts.types.outpost_description
    import aws_sdk_outposts.types.outpost_id
    import aws_sdk_outposts.types.outpost_name
    import aws_sdk_outposts.types.owner_id
    import aws_sdk_outposts.types.site_arn
    import aws_sdk_outposts.types.site_id
    import aws_sdk_outposts.types.supported_hardware_type
    import aws_sdk_outposts.types.tag_map


class Outpost(TypedDict):
    outpost_id: NotRequired["aws_sdk_outposts.types.outpost_id.OutpostId"]
    """<p> The ID of the Outpost. </p>"""
    owner_id: NotRequired["aws_sdk_outposts.types.owner_id.OwnerId"]
    outpost_arn: NotRequired["aws_sdk_outposts.types.outpost_arn.OutpostArn"]
    site_id: NotRequired["aws_sdk_outposts.types.site_id.SiteId"]
    name: NotRequired["aws_sdk_outposts.types.outpost_name.OutpostName"]
    description: NotRequired[
        "aws_sdk_outposts.types.outpost_description.OutpostDescription"
    ]
    life_cycle_status: NotRequired[
        "aws_sdk_outposts.types.life_cycle_status.LifeCycleStatus"
    ]
    availability_zone: NotRequired[
        "aws_sdk_outposts.types.availability_zone.AvailabilityZone"
    ]
    availability_zone_id: NotRequired[
        "aws_sdk_outposts.types.availability_zone_id.AvailabilityZoneId"
    ]
    tags: NotRequired["aws_sdk_outposts.types.tag_map.TagMap"]
    """<p>The Outpost tags.</p>"""
    site_arn: NotRequired["aws_sdk_outposts.types.site_arn.SiteArn"]
    supported_hardware_type: NotRequired[
        "aws_sdk_outposts.types.supported_hardware_type.SupportedHardwareType"
    ]
    """<p> The hardware type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Outpost) -> dict:
    out: dict = {}
    if "outpost_id" in value:
        out["OutpostId"] = value["outpost_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    if "site_id" in value:
        out["SiteId"] = value["site_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "life_cycle_status" in value:
        out["LifeCycleStatus"] = value["life_cycle_status"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "tags" in value:
        import aws_sdk_outposts.types.tag_map

        out["Tags"] = aws_sdk_outposts.types.tag_map.serialize_json(value["tags"])
    if "site_arn" in value:
        out["SiteArn"] = value["site_arn"]
    if "supported_hardware_type" in value:
        import aws_sdk_outposts.types.supported_hardware_type

        out["SupportedHardwareType"] = (
            aws_sdk_outposts.types.supported_hardware_type.serialize_json(
                value["supported_hardware_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> Outpost:
    out: Outpost = {}  # type: ignore[typeddict-item]
    if "OutpostId" in data:
        out["outpost_id"] = data["OutpostId"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "OutpostArn" in data:
        out["outpost_arn"] = data["OutpostArn"]
    if "SiteId" in data:
        out["site_id"] = data["SiteId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LifeCycleStatus" in data:
        out["life_cycle_status"] = data["LifeCycleStatus"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "AvailabilityZoneId" in data:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if "Tags" in data:
        import aws_sdk_outposts.types.tag_map

        out["tags"] = aws_sdk_outposts.types.tag_map.deserialize_json(data["Tags"])
    if "SiteArn" in data:
        out["site_arn"] = data["SiteArn"]
    if "SupportedHardwareType" in data:
        import aws_sdk_outposts.types.supported_hardware_type

        out["supported_hardware_type"] = (
            aws_sdk_outposts.types.supported_hardware_type.deserialize_json(
                data["SupportedHardwareType"]
            )
        )
    return out
