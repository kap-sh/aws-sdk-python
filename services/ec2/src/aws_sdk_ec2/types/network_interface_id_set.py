"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string

NetworkInterfaceIdSet: TypeAlias = list["aws_sdk_ec2.types.string.String"]
