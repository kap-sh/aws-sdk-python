"""Generated from Smithy shape ``com.amazonaws.ec2#DnsServersOptionsModifyStructure``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.value_string_list


class DnsServersOptionsModifyStructure(TypedDict):
    custom_dns_servers: NotRequired[
        "aws_sdk_ec2.types.value_string_list.ValueStringList"
    ]
    """<p>The IPv4 address range, in CIDR notation, of the DNS servers to be used. You can specify up to two DNS servers. Ensure that the DNS servers can be reached by the clients. The specified values overwrite the existing values.</p>"""
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether DNS servers should be used. Specify <code>False</code> to delete the existing DNS servers.</p>"""
