"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstancePlacementRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.affinity
    import aws_sdk_ec2.types.dedicated_host_id
    import aws_sdk_ec2.types.host_tenancy
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.placement_group_id
    import aws_sdk_ec2.types.placement_group_name
    import aws_sdk_ec2.types.string


class ModifyInstancePlacementRequest(TypedDict):
    group_name: NotRequired["aws_sdk_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group in which to place the instance. For spread placement groups, the instance must have a tenancy of <code>default</code>. For cluster and partition placement groups, the instance must have a tenancy of <code>default</code> or <code>dedicated</code>.</p> <p>To remove an instance from a placement group, specify an empty string (\"\").</p>"""
    partition_number: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of the partition in which to place the instance. Valid only if the placement group strategy is set to <code>partition</code>.</p>"""
    host_resource_group_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ARN of the host resource group in which to place the instance. The instance must have a tenancy of <code>host</code> to specify this parameter.</p>"""
    group_id: NotRequired["aws_sdk_ec2.types.placement_group_id.PlacementGroupId"]
    """<p>The Group Id of a placement group. You must specify the Placement Group <b>Group Id</b> to launch an instance in a shared placement group.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance that you are modifying.</p>"""
    tenancy: NotRequired["aws_sdk_ec2.types.host_tenancy.HostTenancy"]
    """<p>The tenancy for the instance.</p> <note> <p>For T3 instances, you must launch the instance on a Dedicated Host to use a tenancy of <code>host</code>. You can't change the tenancy from <code>host</code> to <code>dedicated</code> or <code>default</code>. Attempting to make one of these unsupported tenancy changes results in an <code>InvalidRequest</code> error code.</p> </note>"""
    affinity: NotRequired["aws_sdk_ec2.types.affinity.Affinity"]
    """<p>The affinity setting for the instance. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-affinity\">Host affinity</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    host_id: NotRequired["aws_sdk_ec2.types.dedicated_host_id.DedicatedHostId"]
    """<p>The ID of the Dedicated Host with which to associate the instance.</p>"""
