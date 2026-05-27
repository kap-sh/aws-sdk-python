"""Generated from Smithy shape ``com.amazonaws.ec2#DnsEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DnsEntry(TypedDict):
    dns_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The DNS name.</p>"""
    hosted_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the private hosted zone.</p>"""
