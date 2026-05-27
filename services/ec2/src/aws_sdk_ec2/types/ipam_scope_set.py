"""Generated from Smithy shape ``com.amazonaws.ec2#IpamScopeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_scope

IpamScopeSet: TypeAlias = list["aws_sdk_ec2.types.ipam_scope.IpamScope"]
