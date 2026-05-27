"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceDetailSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_detail

ServiceDetailSet: TypeAlias = list["aws_sdk_ec2.types.service_detail.ServiceDetail"]
