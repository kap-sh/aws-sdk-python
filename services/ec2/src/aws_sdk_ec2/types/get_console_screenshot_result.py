"""Generated from Smithy shape ``com.amazonaws.ec2#GetConsoleScreenshotResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class GetConsoleScreenshotResult(TypedDict):
    image_data: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The data that comprises the image.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
