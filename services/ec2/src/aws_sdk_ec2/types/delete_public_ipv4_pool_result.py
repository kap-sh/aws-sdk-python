"""Generated from Smithy shape ``com.amazonaws.ec2#DeletePublicIpv4PoolResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class DeletePublicIpv4PoolResult(TypedDict):
    return_value: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Information about the result of deleting the public IPv4 pool.</p>"""
