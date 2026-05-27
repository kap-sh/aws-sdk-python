"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyPublicIpDnsNameOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class ModifyPublicIpDnsNameOptionsResult(TypedDict):
    successful: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Whether or not the request was successful.</p>"""
