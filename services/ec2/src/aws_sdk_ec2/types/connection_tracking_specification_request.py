"""Generated from Smithy shape ``com.amazonaws.ec2#ConnectionTrackingSpecificationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class ConnectionTrackingSpecificationRequest(TypedDict):
    tcp_established_timeout: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 432000 seconds. Recommended: Less than 432000 seconds.</p>"""
    udp_stream_timeout: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.</p>"""
    udp_timeout: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.</p>"""
