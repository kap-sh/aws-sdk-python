"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservationTopology``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_node_set
    import aws_sdk_ec2.types.string


class CapacityReservationTopology(TypedDict):
    capacity_reservation_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    capacity_block_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Capacity Block. This parameter is only supported for UltraServer instances and identifies instances within the UltraServer domain.</p>"""
    state: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The current state of the Capacity Reservation. For the list of possible states, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCapacityReservations.html\">DescribeCapacityReservations</a>.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the placement group that the Capacity Reservation is in.</p>"""
    network_nodes: NotRequired["aws_sdk_ec2.types.network_node_set.NetworkNodeSet"]
    """<p>The network nodes. The nodes are hashed based on your account. Capacity Reservations from different accounts running under the same server will return a different hashed list of strings.</p> <p>The value is <code>null</code> or empty if:</p> <ul> <li> <p>The instance type is not supported.</p> </li> <li> <p>The Capacity Reservation is in a state other than <code>active</code> or <code>pending</code>.</p> </li> </ul>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone or Local Zone that the Capacity Reservation is in.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Availability Zone or Local Zone that the Capacity Reservation is in.</p>"""
