"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplatePlacement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tenancy


class LaunchTemplatePlacement(TypedDict):
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the instance.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the instance.</p>"""
    affinity: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The affinity setting for the instance on the Dedicated Host.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the placement group for the instance.</p>"""
    host_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Dedicated Host for the instance.</p>"""
    tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance. An instance with a tenancy of <code>dedicated</code> runs on single-tenant hardware. </p>"""
    spread_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved for future use.</p>"""
    host_resource_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the host resource group in which to launch the instances. </p>"""
    partition_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the partition the instance should launch in. Valid only if the placement group strategy is set to <code>partition</code>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>The Group ID of the placement group. You must specify the Placement Group <b>Group ID</b> to launch an instance in a shared placement group.</p>"""
