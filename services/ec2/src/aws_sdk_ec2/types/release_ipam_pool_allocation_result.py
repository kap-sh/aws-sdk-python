"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseIpamPoolAllocationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class ReleaseIpamPoolAllocationResult(TypedDict):
    success: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates if the release was successful.</p>"""
