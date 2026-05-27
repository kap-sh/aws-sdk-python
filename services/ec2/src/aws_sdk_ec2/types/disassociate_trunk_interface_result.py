"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateTrunkInterfaceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string

DisassociateTrunkInterfaceResult = TypedDict(
    "DisassociateTrunkInterfaceResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "client_token": NotRequired["aws_sdk_ec2.types.string.String"],
    },
)
