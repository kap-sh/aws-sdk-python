"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteNetworkInterfacePermissionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean

DeleteNetworkInterfacePermissionResult = TypedDict(
    "DeleteNetworkInterfacePermissionResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
    },
)
