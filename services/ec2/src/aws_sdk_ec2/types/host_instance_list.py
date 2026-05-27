"""Generated from Smithy shape ``com.amazonaws.ec2#HostInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host_instance

HostInstanceList: TypeAlias = list["aws_sdk_ec2.types.host_instance.HostInstance"]
