"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecurityGroupResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.security_group_id

DeleteSecurityGroupResult = TypedDict(
    "DeleteSecurityGroupResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
        "group_id": NotRequired["aws_sdk_ec2.types.security_group_id.SecurityGroupId"],
    },
)
