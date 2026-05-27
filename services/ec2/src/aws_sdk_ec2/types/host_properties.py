"""Generated from Smithy shape ``com.amazonaws.ec2#HostProperties``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string


class HostProperties(TypedDict):
    cores: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of cores on the Dedicated Host.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance type supported by the Dedicated Host. For example, <code>m5.large</code>. If the host supports multiple instance types, no <b>instanceType</b> is returned.</p>"""
    instance_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The instance family supported by the Dedicated Host. For example, <code>m5</code>.</p>"""
    sockets: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of sockets on the Dedicated Host.</p>"""
    total_v_cpus: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The total number of vCPUs on the Dedicated Host.</p>"""
