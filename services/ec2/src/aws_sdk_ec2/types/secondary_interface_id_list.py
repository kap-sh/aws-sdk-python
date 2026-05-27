"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfaceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_interface_id

SecondaryInterfaceIdList: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_interface_id.SecondaryInterfaceId"
]
