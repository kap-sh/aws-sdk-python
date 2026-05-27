"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTopology``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_nodes_list
    import aws_sdk_ec2.types.string


class InstanceTopology(TypedDict):
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance ID.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the placement group that the instance is in.</p>"""
    network_nodes: NotRequired["aws_sdk_ec2.types.network_nodes_list.NetworkNodesList"]
    """<p>The network nodes. The nodes are hashed based on your account. Instances from different accounts running under the same server will return a different hashed list of strings.</p> <p>The value is <code>null</code> or empty if:</p> <ul> <li> <p>The instance type is not supported.</p> </li> <li> <p>The instance is in a state other than <code>running</code>.</p> </li> </ul>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Availability Zone or Local Zone that the instance is in.</p>"""
    zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone or Local Zone that the instance is in.</p>"""
    capacity_block_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Block. This parameter is only supported for UltraServer instances and identifies instances within the UltraServer domain.</p>"""
