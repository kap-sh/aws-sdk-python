"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkAclIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_acl_id

NetworkAclIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.network_acl_id.NetworkAclId"
]
