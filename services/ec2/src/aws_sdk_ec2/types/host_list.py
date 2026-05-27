"""Generated from Smithy shape ``com.amazonaws.ec2#HostList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.host

HostList: TypeAlias = list["aws_sdk_ec2.types.host.Host"]
