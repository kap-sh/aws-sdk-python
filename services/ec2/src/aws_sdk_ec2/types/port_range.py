"""Generated from Smithy shape ``com.amazonaws.ec2#PortRange``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer

PortRange = TypedDict(
    "PortRange",
    {
        "from": NotRequired["aws_sdk_ec2.types.integer.Integer"],
        "to": NotRequired["aws_sdk_ec2.types.integer.Integer"],
    },
)
