"""Generated from Smithy shape ``com.amazonaws.ec2#VgwTelemetry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.telemetry_status


class VgwTelemetry(TypedDict):
    accepted_route_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accepted routes.</p>"""
    last_status_change: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time of the last change in status. This field is updated when changes in IKE (Phase 1), IPSec (Phase 2), or BGP status are detected.</p>"""
    outside_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Internet-routable IP address of the virtual private gateway's outside interface.</p>"""
    status: NotRequired["aws_sdk_ec2.types.telemetry_status.TelemetryStatus"]
    """<p>The status of the VPN tunnel.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If an error occurs, a description of the error.</p>"""
    certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the VPN tunnel endpoint certificate.</p>"""
