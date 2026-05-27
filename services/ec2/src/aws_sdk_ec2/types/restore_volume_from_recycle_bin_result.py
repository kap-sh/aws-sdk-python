"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreVolumeFromRecycleBinResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean

RestoreVolumeFromRecycleBinResult = TypedDict(
    "RestoreVolumeFromRecycleBinResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
    },
)
