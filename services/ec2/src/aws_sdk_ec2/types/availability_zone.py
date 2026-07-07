"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZone``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_geography_list
    import aws_sdk_ec2.types.availability_zone_message_list
    import aws_sdk_ec2.types.availability_zone_opt_in_status
    import aws_sdk_ec2.types.availability_zone_state
    import aws_sdk_ec2.types.availability_zone_sub_geography_list
    import aws_sdk_ec2.types.string


class AvailabilityZone(TypedDict, closed=True):
    opt_in_status: NotRequired[
        "aws_sdk_ec2.types.availability_zone_opt_in_status.AvailabilityZoneOptInStatus"
    ]
    """<p>For Availability Zones, this parameter always has the value of <code>opt-in-not-required</code>.</p> <p>For Local Zones and Wavelength Zones, this parameter is the opt-in status. The possible values are <code>opted-in</code> and <code>not-opted-in</code>.</p>"""
    messages: NotRequired[
        "aws_sdk_ec2.types.availability_zone_message_list.AvailabilityZoneMessageList"
    ]
    """<p>Any messages about the Availability Zone, Local Zone, or Wavelength Zone.</p>"""
    region_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Region.</p>"""
    zone_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Availability Zone, Local Zone, or Wavelength Zone.</p>"""
    zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone, Local Zone, or Wavelength Zone.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the zone group. For example:</p> <ul> <li> <p>Availability Zones - <code>us-east-1-zg-1</code> </p> </li> <li> <p>Local Zones - <code>us-west-2-lax-1</code> </p> </li> <li> <p>Wavelength Zones - <code>us-east-1-wl1-bos-wlz-1</code> </p> </li> </ul>"""
    network_border_group: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the network border group.</p>"""
    zone_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of zone.</p> <p>Valid values: <code>availability-zone</code> | <code>local-zone</code> | <code>wavelength-zone</code> </p>"""
    parent_zone_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls.</p>"""
    parent_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls.</p>"""
    group_long_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The long name of the Availability Zone group, Local Zone group, or Wavelength Zone group.</p>"""
    geography: NotRequired[
        "aws_sdk_ec2.types.availability_zone_geography_list.AvailabilityZoneGeographyList"
    ]
    """<p>The geography information for the Availability Zone or Local Zone. The geography is returned as a list.</p>"""
    sub_geography: NotRequired[
        "aws_sdk_ec2.types.availability_zone_sub_geography_list.AvailabilityZoneSubGeographyList"
    ]
    """<p>The sub-geography information for the Availability Zone or Local Zone. The sub-geography is returned as a list.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.availability_zone_state.AvailabilityZoneState"
    ]
    """<p>The state of the Availability Zone, Local Zone, or Wavelength Zone. The possible values are <code>available</code>, <code>unavailable</code>, and <code>constrained</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZone, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "opt_in_status" in value:
        import aws_sdk_ec2.types.availability_zone_opt_in_status

        aws_sdk_ec2.types.availability_zone_opt_in_status.serialize_ec2_query(
            value["opt_in_status"], pairs, f"{prefix}.OptInStatus"
        )
    if "messages" in value:
        import aws_sdk_ec2.types.availability_zone_message_list

        aws_sdk_ec2.types.availability_zone_message_list.serialize_ec2_query(
            value["messages"], pairs, f"{prefix}.MessageSet"
        )
    if "region_name" in value:
        pairs.append((f"{prefix}.RegionName", str(value["region_name"])))
    if "zone_name" in value:
        pairs.append((f"{prefix}.ZoneName", str(value["zone_name"])))
    if "zone_id" in value:
        pairs.append((f"{prefix}.ZoneId", str(value["zone_id"])))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))
    if "network_border_group" in value:
        pairs.append(
            (f"{prefix}.NetworkBorderGroup", str(value["network_border_group"]))
        )
    if "zone_type" in value:
        pairs.append((f"{prefix}.ZoneType", str(value["zone_type"])))
    if "parent_zone_name" in value:
        pairs.append((f"{prefix}.ParentZoneName", str(value["parent_zone_name"])))
    if "parent_zone_id" in value:
        pairs.append((f"{prefix}.ParentZoneId", str(value["parent_zone_id"])))
    if "group_long_name" in value:
        pairs.append((f"{prefix}.GroupLongName", str(value["group_long_name"])))
    if "geography" in value:
        import aws_sdk_ec2.types.availability_zone_geography_list

        aws_sdk_ec2.types.availability_zone_geography_list.serialize_ec2_query(
            value["geography"], pairs, f"{prefix}.GeographySet"
        )
    if "sub_geography" in value:
        import aws_sdk_ec2.types.availability_zone_sub_geography_list

        aws_sdk_ec2.types.availability_zone_sub_geography_list.serialize_ec2_query(
            value["sub_geography"], pairs, f"{prefix}.SubGeographySet"
        )
    if "state" in value:
        import aws_sdk_ec2.types.availability_zone_state

        aws_sdk_ec2.types.availability_zone_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.ZoneState"
        )


def deserialize_ec2_query(el: Element) -> AvailabilityZone:
    out: AvailabilityZone = {}  # type: ignore[typeddict-item]
    child_opt_in_status = el.find("OptInStatus")
    if child_opt_in_status is not None:
        import aws_sdk_ec2.types.availability_zone_opt_in_status

        out["opt_in_status"] = (
            aws_sdk_ec2.types.availability_zone_opt_in_status.deserialize_ec2_query(
                child_opt_in_status
            )
        )
    if el.find("MessageSet") is not None:
        import aws_sdk_ec2.types.availability_zone_message_list

        out["messages"] = (
            aws_sdk_ec2.types.availability_zone_message_list.deserialize_ec2_query(
                el, "MessageSet"
            )
        )
    child_region_name = el.find("RegionName")
    if child_region_name is not None:
        out["region_name"] = str(child_region_name.text or "")
    child_zone_name = el.find("ZoneName")
    if child_zone_name is not None:
        out["zone_name"] = str(child_zone_name.text or "")
    child_zone_id = el.find("ZoneId")
    if child_zone_id is not None:
        out["zone_id"] = str(child_zone_id.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_network_border_group = el.find("NetworkBorderGroup")
    if child_network_border_group is not None:
        out["network_border_group"] = str(child_network_border_group.text or "")
    child_zone_type = el.find("ZoneType")
    if child_zone_type is not None:
        out["zone_type"] = str(child_zone_type.text or "")
    child_parent_zone_name = el.find("ParentZoneName")
    if child_parent_zone_name is not None:
        out["parent_zone_name"] = str(child_parent_zone_name.text or "")
    child_parent_zone_id = el.find("ParentZoneId")
    if child_parent_zone_id is not None:
        out["parent_zone_id"] = str(child_parent_zone_id.text or "")
    child_group_long_name = el.find("GroupLongName")
    if child_group_long_name is not None:
        out["group_long_name"] = str(child_group_long_name.text or "")
    if el.find("GeographySet") is not None:
        import aws_sdk_ec2.types.availability_zone_geography_list

        out["geography"] = (
            aws_sdk_ec2.types.availability_zone_geography_list.deserialize_ec2_query(
                el, "GeographySet"
            )
        )
    if el.find("SubGeographySet") is not None:
        import aws_sdk_ec2.types.availability_zone_sub_geography_list

        out["sub_geography"] = (
            aws_sdk_ec2.types.availability_zone_sub_geography_list.deserialize_ec2_query(
                el, "SubGeographySet"
            )
        )
    child_state = el.find("ZoneState")
    if child_state is not None:
        import aws_sdk_ec2.types.availability_zone_state

        out["state"] = aws_sdk_ec2.types.availability_zone_state.deserialize_ec2_query(
            child_state
        )
    return out
