"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZone``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_geography_list
    import aws_sdk_ec2.types.availability_zone_message_list
    import aws_sdk_ec2.types.availability_zone_opt_in_status
    import aws_sdk_ec2.types.availability_zone_state
    import aws_sdk_ec2.types.availability_zone_sub_geography_list
    import aws_sdk_ec2.types.string


class AvailabilityZone(TypedDict):
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
