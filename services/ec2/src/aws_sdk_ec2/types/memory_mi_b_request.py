"""Generated from Smithy shape ``com.amazonaws.ec2#MemoryMiBRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class MemoryMiBRequest(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum amount of memory, in MiB. To specify no minimum limit, specify <code>0</code>.</p>"""
    max: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum amount of memory, in MiB. To specify no maximum limit, omit this parameter.</p>"""
