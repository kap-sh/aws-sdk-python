"""Generated from Smithy shape ``com.amazonaws.ec2#CancelBundleTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bundle_task


class CancelBundleTaskResult(TypedDict):
    bundle_task: NotRequired["aws_sdk_ec2.types.bundle_task.BundleTask"]
    """<p>Information about the bundle task.</p>"""
