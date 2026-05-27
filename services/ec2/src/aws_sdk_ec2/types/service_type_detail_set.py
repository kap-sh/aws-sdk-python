"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceTypeDetailSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_type_detail

ServiceTypeDetailSet: TypeAlias = list[
    "aws_sdk_ec2.types.service_type_detail.ServiceTypeDetail"
]
