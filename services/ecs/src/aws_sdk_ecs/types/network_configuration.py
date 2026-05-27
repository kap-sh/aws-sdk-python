"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.aws_vpc_configuration


class NetworkConfiguration(TypedDict):
    awsvpc_configuration: NotRequired[
        "aws_sdk_ecs.types.aws_vpc_configuration.AwsVpcConfiguration"
    ]
    """<p>The VPC subnets and security groups that are associated with a task.</p> <note> <p>All specified subnets and security groups must be from the same VPC.</p> </note>"""
