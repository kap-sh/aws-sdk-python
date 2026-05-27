"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceConnectEndpointDnsNames``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class InstanceConnectEndpointDnsNames(TypedDict):
    dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name of the EC2 Instance Connect Endpoint.</p>"""
    fips_dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Federal Information Processing Standards (FIPS) compliant DNS name of the EC2 Instance Connect Endpoint.</p>"""
