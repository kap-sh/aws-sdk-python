"""Generated from Smithy shape ``com.amazonaws.ec2#Phase1DHGroupNumbersListValue``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class Phase1DHGroupNumbersListValue(TypedDict):
    value: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Diffie-Hellmann group number.</p>"""
