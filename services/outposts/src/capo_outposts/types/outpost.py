"""Generated from Smithy shape ``com.amazonaws.outposts#Outpost``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.availability_zone
    import capo_outposts.types.availability_zone_id
    import capo_outposts.types.life_cycle_status
    import capo_outposts.types.outpost_arn
    import capo_outposts.types.outpost_description
    import capo_outposts.types.outpost_id
    import capo_outposts.types.outpost_name
    import capo_outposts.types.owner_id
    import capo_outposts.types.site_arn
    import capo_outposts.types.site_id
    import capo_outposts.types.supported_hardware_type
    import capo_outposts.types.tag_map


class Outpost(TypedDict, closed=True):
    outpost_id: NotRequired["capo_outposts.types.outpost_id.OutpostId"]
    """<p> The ID of the Outpost. </p>"""
    owner_id: NotRequired["capo_outposts.types.owner_id.OwnerId"]
    outpost_arn: NotRequired["capo_outposts.types.outpost_arn.OutpostArn"]
    site_id: NotRequired["capo_outposts.types.site_id.SiteId"]
    name: NotRequired["capo_outposts.types.outpost_name.OutpostName"]
    description: NotRequired[
        "capo_outposts.types.outpost_description.OutpostDescription"
    ]
    life_cycle_status: NotRequired[
        "capo_outposts.types.life_cycle_status.LifeCycleStatus"
    ]
    availability_zone: NotRequired[
        "capo_outposts.types.availability_zone.AvailabilityZone"
    ]
    availability_zone_id: NotRequired[
        "capo_outposts.types.availability_zone_id.AvailabilityZoneId"
    ]
    tags: NotRequired["capo_outposts.types.tag_map.TagMap"]
    """<p>The Outpost tags.</p>"""
    site_arn: NotRequired["capo_outposts.types.site_arn.SiteArn"]
    supported_hardware_type: NotRequired[
        "capo_outposts.types.supported_hardware_type.SupportedHardwareType"
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
        import capo_outposts.types.tag_map

        out["Tags"] = capo_outposts.types.tag_map.serialize_json(value["tags"])
    if "site_arn" in value:
        out["SiteArn"] = value["site_arn"]
    if "supported_hardware_type" in value:
        import capo_outposts.types.supported_hardware_type

        out["SupportedHardwareType"] = (
            capo_outposts.types.supported_hardware_type.serialize_json(
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
        import capo_outposts.types.tag_map

        out["tags"] = capo_outposts.types.tag_map.deserialize_json(data["Tags"])
    if "SiteArn" in data:
        out["site_arn"] = data["SiteArn"]
    if "SupportedHardwareType" in data:
        import capo_outposts.types.supported_hardware_type

        out["supported_hardware_type"] = (
            capo_outposts.types.supported_hardware_type.deserialize_json(
                data["SupportedHardwareType"]
            )
        )
    return out
