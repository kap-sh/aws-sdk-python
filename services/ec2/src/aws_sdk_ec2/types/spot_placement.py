"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPlacement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tenancy


class SpotPlacement(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone. For example, <code>us-east-2a</code>.</p> <p>[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, \"<code>us-east-2a</code>, <code>us-east-2b</code>\".</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group.</p>"""
    tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of <code>dedicated</code> runs on single-tenant hardware. The <code>host</code> tenancy is not supported for Spot Instances.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone. For example, <code>use2-az1</code>.</p> <p>[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, \"<code>use2-az1</code>, <code>use2-bz1</code>\".</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
