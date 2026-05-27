"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveredAccount``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_discovery_failure_reason
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class IpamDiscoveredAccount(TypedDict):
    account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The account ID.</p>"""
    discovery_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services Region that the account information is returned from. An account can be discovered in multiple regions and will have a separate discovered account for each Region.</p>"""
    failure_reason: NotRequired[
        "aws_sdk_ec2.types.ipam_discovery_failure_reason.IpamDiscoveryFailureReason"
    ]
    """<p>The resource discovery failure reason.</p>"""
    last_attempted_discovery_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last attempted resource discovery time.</p>"""
    last_successful_discovery_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The last successful resource discovery time.</p>"""
    organizational_unit_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of an Organizational Unit in Amazon Web Services Organizations.</p>"""
