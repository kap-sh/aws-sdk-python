"""Generated from Smithy shape ``com.amazonaws.ec2#DefaultConnectionTrackingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.default_tcp_established_timeout
    import aws_sdk_ec2.types.default_udp_stream_timeout
    import aws_sdk_ec2.types.default_udp_timeout


class DefaultConnectionTrackingConfiguration(TypedDict):
    default_tcp_established_timeout: NotRequired[
        "aws_sdk_ec2.types.default_tcp_established_timeout.DefaultTcpEstablishedTimeout"
    ]
    """<p>Default timeout (in seconds) for idle TCP connections in an established state.</p>"""
    default_udp_timeout: NotRequired[
        "aws_sdk_ec2.types.default_udp_timeout.DefaultUdpTimeout"
    ]
    """<p>Default timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction.</p>"""
    default_udp_stream_timeout: NotRequired[
        "aws_sdk_ec2.types.default_udp_stream_timeout.DefaultUdpStreamTimeout"
    ]
    """<p>Default timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction.</p>"""
