"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAvailabilityZonesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_list


class DescribeAvailabilityZonesResult(TypedDict):
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>Information about the Availability Zones, Local Zones, and Wavelength Zones.</p>"""
