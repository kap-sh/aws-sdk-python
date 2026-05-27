"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoresRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_id_string_list
    import aws_sdk_ec2.types.availability_zone_string_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.snapshot_id_string_list


class EnableFastSnapshotRestoresRequest(TypedDict):
    availability_zones: NotRequired[
        "aws_sdk_ec2.types.availability_zone_string_list.AvailabilityZoneStringList"
    ]
    """<p>One or more Availability Zones. For example, <code>us-east-2a</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_ec2.types.availability_zone_id_string_list.AvailabilityZoneIdStringList"
    ]
    """<p>One or more Availability Zone IDs. For example, <code>use2-az1</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    source_snapshot_ids: NotRequired[
        "aws_sdk_ec2.types.snapshot_id_string_list.SnapshotIdStringList"
    ]
    """<p>The IDs of one or more snapshots. For example, <code>snap-1234567890abcdef0</code>. You can specify a snapshot that was shared with you from another Amazon Web Services account.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
