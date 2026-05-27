"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesNetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string_list


class ManagedInstancesNetworkConfiguration(TypedDict):
    subnets: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of subnet IDs where Amazon ECS can launch Amazon ECS Managed Instances. Instances are distributed across the specified subnets for high availability. All subnets must be in the same VPC.</p>"""
    security_groups: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The list of security group IDs to apply to Amazon ECS Managed Instances. These security groups control the network traffic allowed to and from the instances.</p>"""
