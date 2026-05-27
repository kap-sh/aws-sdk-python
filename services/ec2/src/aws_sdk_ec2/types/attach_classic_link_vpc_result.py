"""Generated from Smithy shape ``com.amazonaws.ec2#AttachClassicLinkVpcResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean

AttachClassicLinkVpcResult = TypedDict(
    "AttachClassicLinkVpcResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
    },
)
