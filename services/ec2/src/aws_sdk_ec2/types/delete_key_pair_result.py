"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteKeyPairResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string

DeleteKeyPairResult = TypedDict(
    "DeleteKeyPairResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "key_pair_id": NotRequired["aws_sdk_ec2.types.string.String"],
    },
)
