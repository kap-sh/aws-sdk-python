"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsNameConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dns_name_state
    import aws_sdk_ec2.types.string


class PrivateDnsNameConfiguration(TypedDict):
    state: NotRequired["aws_sdk_ec2.types.dns_name_state.DnsNameState"]
    """<p>The verification state of the VPC endpoint service.</p> <p>Consumers of the endpoint service can use the private name only when the state is <code>verified</code>.</p>"""
    type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The endpoint service verification type, for example TXT.</p>"""
    value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The value the service provider adds to the private DNS name domain record before verification.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the record subdomain the service provider needs to create. The service provider adds the <code>value</code> text to the <code>name</code>.</p>"""
