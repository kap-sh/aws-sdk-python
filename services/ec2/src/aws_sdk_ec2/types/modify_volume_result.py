"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVolumeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.volume_modification


class ModifyVolumeResult(TypedDict):
    volume_modification: NotRequired[
        "aws_sdk_ec2.types.volume_modification.VolumeModification"
    ]
    """<p>Information about the volume modification.</p>"""
