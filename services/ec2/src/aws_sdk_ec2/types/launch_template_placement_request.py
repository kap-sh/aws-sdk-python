"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplatePlacementRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.dedicated_host_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tenancy


class LaunchTemplatePlacementRequest(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone for the instance.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone for the instance.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> can be specified, but not both</p>"""
    affinity: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The affinity setting for an instance on a Dedicated Host.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group for the instance.</p>"""
    host_id: NotRequired["aws_sdk_ec2.types.dedicated_host_id.DedicatedHostId"]
    """<p>The ID of the Dedicated Host for the instance.</p>"""
    tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance. An instance with a tenancy of dedicated runs on single-tenant hardware.</p>"""
    spread_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved for future use.</p>"""
    host_resource_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the host resource group in which to launch the instances. If you specify a host resource group ARN, omit the <b>Tenancy</b> parameter or set it to <code>host</code>.</p>"""
    partition_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the partition the instance should launch in. Valid only if the placement group strategy is set to <code>partition</code>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>The Group Id of a placement group. You must specify the Placement Group <b>Group Id</b> to launch an instance in a shared placement group.</p>"""
