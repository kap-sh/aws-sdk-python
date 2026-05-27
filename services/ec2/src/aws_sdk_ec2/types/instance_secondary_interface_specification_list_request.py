"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfaceSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_secondary_interface_specification_request

InstanceSecondaryInterfaceSpecificationListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.instance_secondary_interface_specification_request.InstanceSecondaryInterfaceSpecificationRequest"
]
