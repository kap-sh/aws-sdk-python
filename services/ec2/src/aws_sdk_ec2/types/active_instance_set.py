"""Generated from Smithy shape ``com.amazonaws.ec2#ActiveInstanceSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.active_instance

ActiveInstanceSet: TypeAlias = list["aws_sdk_ec2.types.active_instance.ActiveInstance"]
