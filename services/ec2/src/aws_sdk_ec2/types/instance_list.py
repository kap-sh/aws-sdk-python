"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance

InstanceList: TypeAlias = list["aws_sdk_ec2.types.instance.Instance"]
