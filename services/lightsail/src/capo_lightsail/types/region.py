"""Generated from Smithy shape ``com.amazonaws.lightsail#Region``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.availability_zone_list
    import capo_lightsail.types.region_name
    import capo_lightsail.types.string


class Region(TypedDict, closed=True):
    continent_code: NotRequired["capo_lightsail.types.string.string"]
    """<p>The continent code (<code>NA</code>, meaning North America).</p>"""
    description: NotRequired["capo_lightsail.types.string.string"]
    """<p>The description of the Amazon Web Services Region (<code>This region is recommended to serve users in the eastern United States and eastern Canada</code>).</p>"""
    display_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The display name (<code>Ohio</code>).</p>"""
    name: NotRequired["capo_lightsail.types.region_name.RegionName"]
    """<p>The region name (<code>us-east-2</code>).</p>"""
    availability_zones: NotRequired[
        "capo_lightsail.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>The Availability Zones. Follows the format <code>us-east-2a</code> (case-sensitive).</p>"""
    relational_database_availability_zones: NotRequired[
        "capo_lightsail.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>The Availability Zones for databases. Follows the format <code>us-east-2a</code> (case-sensitive).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Region) -> dict:
    out: dict = {}
    if "continent_code" in value:
        out["continentCode"] = value["continent_code"]
    if "description" in value:
        out["description"] = value["description"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "name" in value:
        import capo_lightsail.types.region_name

        out["name"] = capo_lightsail.types.region_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "availability_zones" in value:
        import capo_lightsail.types.availability_zone_list

        out["availabilityZones"] = (
            capo_lightsail.types.availability_zone_list.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "relational_database_availability_zones" in value:
        import capo_lightsail.types.availability_zone_list

        out["relationalDatabaseAvailabilityZones"] = (
            capo_lightsail.types.availability_zone_list.serialize_aws_json_1_1(
                value["relational_database_availability_zones"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Region:
    out: Region = {}  # type: ignore[typeddict-item]
    if "continentCode" in data:
        out["continent_code"] = data["continentCode"]
    if "description" in data:
        out["description"] = data["description"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "name" in data:
        import capo_lightsail.types.region_name

        out["name"] = capo_lightsail.types.region_name.deserialize_aws_json_1_1(
            data["name"]
        )
    if "availabilityZones" in data:
        import capo_lightsail.types.availability_zone_list

        out["availability_zones"] = (
            capo_lightsail.types.availability_zone_list.deserialize_aws_json_1_1(
                data["availabilityZones"]
            )
        )
    if "relationalDatabaseAvailabilityZones" in data:
        import capo_lightsail.types.availability_zone_list

        out["relational_database_availability_zones"] = (
            capo_lightsail.types.availability_zone_list.deserialize_aws_json_1_1(
                data["relationalDatabaseAvailabilityZones"]
            )
        )
    return out
