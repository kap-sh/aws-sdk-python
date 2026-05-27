"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorTotalMemoryMiB``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class AcceleratorTotalMemoryMiB(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum amount of accelerator memory, in MiB. If this parameter is not specified, there is no minimum limit.</p>"""
    max: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum amount of accelerator memory, in MiB. If this parameter is not specified, there is no maximum limit.</p>"""
