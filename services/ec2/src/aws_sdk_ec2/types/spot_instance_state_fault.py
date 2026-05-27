"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceStateFault``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SpotInstanceStateFault(TypedDict):
    code: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason code for the Spot Instance state change.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The message for the Spot Instance state change.</p>"""
