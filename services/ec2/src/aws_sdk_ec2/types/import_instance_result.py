"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.conversion_task


class ImportInstanceResult(TypedDict):
    conversion_task: NotRequired["aws_sdk_ec2.types.conversion_task.ConversionTask"]
    """<p>Information about the conversion task.</p>"""
