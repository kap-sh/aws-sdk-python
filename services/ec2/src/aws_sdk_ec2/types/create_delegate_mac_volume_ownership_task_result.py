"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDelegateMacVolumeOwnershipTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_modification_task


class CreateDelegateMacVolumeOwnershipTaskResult(TypedDict):
    mac_modification_task: NotRequired[
        "aws_sdk_ec2.types.mac_modification_task.MacModificationTask"
    ]
    """<p>Information about the volume ownership delegation task.</p>"""
