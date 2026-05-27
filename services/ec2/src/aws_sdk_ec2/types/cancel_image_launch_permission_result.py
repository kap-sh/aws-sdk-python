"""Generated from Smithy shape ``com.amazonaws.ec2#CancelImageLaunchPermissionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean

CancelImageLaunchPermissionResult = TypedDict(
    "CancelImageLaunchPermissionResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
    },
)
