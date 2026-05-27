"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyFleetResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean

ModifyFleetResult = TypedDict(
    "ModifyFleetResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
    },
)
