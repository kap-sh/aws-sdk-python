"""Generated from Smithy shape ``com.amazonaws.ec2#Host``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocation_state
    import aws_sdk_ec2.types.allows_multiple_instance_types
    import aws_sdk_ec2.types.asset_id
    import aws_sdk_ec2.types.auto_placement
    import aws_sdk_ec2.types.available_capacity
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.host_instance_list
    import aws_sdk_ec2.types.host_maintenance
    import aws_sdk_ec2.types.host_properties
    import aws_sdk_ec2.types.host_recovery
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class Host(TypedDict):
    auto_placement: NotRequired["aws_sdk_ec2.types.auto_placement.AutoPlacement"]
    """<p>Whether auto-placement is on or off.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone of the Dedicated Host.</p>"""
    available_capacity: NotRequired[
        "aws_sdk_ec2.types.available_capacity.AvailableCapacity"
    ]
    """<p>Information about the instances running on the Dedicated Host.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring Idempotency</a>.</p>"""
    host_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Dedicated Host.</p>"""
    host_properties: NotRequired["aws_sdk_ec2.types.host_properties.HostProperties"]
    """<p>The hardware specifications of the Dedicated Host.</p>"""
    host_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reservation ID of the Dedicated Host. This returns a <code>null</code> response if the Dedicated Host doesn't have an associated reservation.</p>"""
    instances: NotRequired["aws_sdk_ec2.types.host_instance_list.HostInstanceList"]
    """<p>The IDs and instance type that are currently running on the Dedicated Host.</p>"""
    state: NotRequired["aws_sdk_ec2.types.allocation_state.AllocationState"]
    """<p>The Dedicated Host's state.</p>"""
    allocation_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that the Dedicated Host was allocated.</p>"""
    release_time: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The time that the Dedicated Host was released.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Dedicated Host.</p>"""
    host_recovery: NotRequired["aws_sdk_ec2.types.host_recovery.HostRecovery"]
    """<p>Indicates whether host recovery is enabled or disabled for the Dedicated Host.</p>"""
    allows_multiple_instance_types: NotRequired[
        "aws_sdk_ec2.types.allows_multiple_instance_types.AllowsMultipleInstanceTypes"
    ]
    """<p>Indicates whether the Dedicated Host supports multiple instance types of the same instance family. If the value is <code>on</code>, the Dedicated Host supports multiple instance types in the instance family. If the value is <code>off</code>, the Dedicated Host supports a single instance type only.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Dedicated Host.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the Dedicated Host is allocated.</p>"""
    member_of_service_linked_resource_group: NotRequired[
        "aws_sdk_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether the Dedicated Host is in a host resource group. If <b>memberOfServiceLinkedResourceGroup</b> is <code>true</code>, the host is in a host resource group; otherwise, it is not.</p>"""
    outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which the Dedicated Host is allocated.</p>"""
    host_maintenance: NotRequired["aws_sdk_ec2.types.host_maintenance.HostMaintenance"]
    """<p>Indicates whether host maintenance is enabled or disabled for the Dedicated Host.</p>"""
    asset_id: NotRequired["aws_sdk_ec2.types.asset_id.AssetId"]
    """<p>The ID of the Outpost hardware asset on which the Dedicated Host is allocated.</p>"""
