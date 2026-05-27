"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStatusDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_status_details

InstanceStatusDetailsList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_status_details.InstanceStatusDetails"
]
