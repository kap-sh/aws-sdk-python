"""Generated from Smithy shape ``com.amazonaws.ec2#CreateReplaceRootVolumeTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_root_volume_task


class CreateReplaceRootVolumeTaskResult(TypedDict):
    replace_root_volume_task: NotRequired[
        "aws_sdk_ec2.types.replace_root_volume_task.ReplaceRootVolumeTask"
    ]
    """<p>Information about the root volume replacement task.</p>"""
