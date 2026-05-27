"""Generated from Smithy shape ``com.amazonaws.ec2#CreateMacSystemIntegrityProtectionModificationTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_modification_task


class CreateMacSystemIntegrityProtectionModificationTaskResult(TypedDict):
    mac_modification_task: NotRequired[
        "aws_sdk_ec2.types.mac_modification_task.MacModificationTask"
    ]
    """<p>Information about the SIP modification task.</p>"""
