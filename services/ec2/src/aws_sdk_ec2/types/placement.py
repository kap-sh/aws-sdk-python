"""Generated from Smithy shape ``com.amazonaws.ec2#Placement``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tenancy


class Placement(TypedDict):
    availability_zone_id: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone of the instance.</p> <p>On input, you can specify <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code>, but not both. If you specify neither one, Amazon EC2 automatically selects an Availability Zone for you.</p> <p>This parameter is not supported for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet\">CreateFleet</a>.</p>"""
    affinity: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The affinity setting for the instance on the Dedicated Host.</p> <p>This parameter is not supported for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet\">CreateFleet</a> or <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html\">ImportInstance</a>.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group that the instance is in.</p> <p>On input, you can specify <code>GroupId</code> or <code>GroupName</code>, but not both.</p>"""
    partition_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the partition that the instance is in. Valid only if the placement group strategy is set to <code>partition</code>.</p> <p>This parameter is not supported for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet\">CreateFleet</a>.</p>"""
    host_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Dedicated Host on which the instance resides.</p> <p>This parameter is not supported for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet\">CreateFleet</a> or <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html\">ImportInstance</a>.</p>"""
    tenancy: NotRequired["aws_sdk_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance. An instance with a tenancy of <code>dedicated</code> runs on single-tenant hardware.</p> <p>This parameter is not supported for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet\">CreateFleet</a>. The <code>host</code> tenancy is not supported for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportInstance.html\">ImportInstance</a> or for T3 instances that are configured for the <code>unlimited</code> CPU credit option.</p>"""
    spread_domain: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Reserved for future use.</p>"""
    host_resource_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the host resource group in which to launch the instances.</p> <p>On input, if you specify this parameter, either omit the <b>Tenancy</b> parameter or set it to <code>host</code>.</p> <p>This parameter is not supported for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet\">CreateFleet</a>.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>The ID of the placement group that the instance is in.</p> <p>On input, you can specify <code>GroupId</code> or <code>GroupName</code>, but not both.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the instance.</p> <p>On input, you can specify <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code>, but not both. If you specify neither one, Amazon EC2 automatically selects an Availability Zone for you.</p> <p>This parameter is not supported for <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet\">CreateFleet</a>.</p>"""
