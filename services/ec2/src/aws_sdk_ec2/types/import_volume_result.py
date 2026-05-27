"""Generated from Smithy shape ``com.amazonaws.ec2#ImportVolumeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.conversion_task


class ImportVolumeResult(TypedDict):
    conversion_task: NotRequired["aws_sdk_ec2.types.conversion_task.ConversionTask"]
    """<p>Information about the conversion task.</p>"""
