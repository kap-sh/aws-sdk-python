"""Generated from Smithy shape ``com.amazonaws.ec2#MacHostList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_host

MacHostList: TypeAlias = list["aws_sdk_ec2.types.mac_host.MacHost"]
