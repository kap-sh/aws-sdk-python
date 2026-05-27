"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesProvider``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_repair_configuration
    import aws_sdk_ecs.types.infrastructure_optimization
    import aws_sdk_ecs.types.instance_launch_template
    import aws_sdk_ecs.types.propagate_mi_tags
    import aws_sdk_ecs.types.string


class ManagedInstancesProvider(TypedDict):
    infrastructure_role_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the infrastructure role that Amazon ECS assumes to manage instances. This role must include permissions for Amazon EC2 instance lifecycle management, networking, and any additional Amazon Web Services services required for your workloads.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html\">Amazon ECS infrastructure IAM role</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    instance_launch_template: NotRequired[
        "aws_sdk_ecs.types.instance_launch_template.InstanceLaunchTemplate"
    ]
    """<p>The launch template that defines how Amazon ECS launches Amazon ECS Managed Instances. This includes the instance profile for your tasks, network and storage configuration, and instance requirements that determine which Amazon EC2 instance types can be used.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html\">Store instance launch parameters in Amazon EC2 launch templates</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    propagate_tags: NotRequired["aws_sdk_ecs.types.propagate_mi_tags.PropagateMITags"]
    """<p>Determines whether tags from the capacity provider are automatically applied to Amazon ECS Managed Instances. This helps with cost allocation and resource management by ensuring consistent tagging across your infrastructure.</p>"""
    infrastructure_optimization: NotRequired[
        "aws_sdk_ecs.types.infrastructure_optimization.InfrastructureOptimization"
    ]
    """<p>Defines how Amazon ECS Managed Instances optimizes the infrastastructure in your capacity provider. Configure it to turn on or off the infrastructure optimization in your capacity provider, and to control the idle or underutilized EC2 instances optimization delay.</p>"""
    auto_repair_configuration: NotRequired[
        "aws_sdk_ecs.types.auto_repair_configuration.AutoRepairConfiguration"
    ]
    """<p>The auto repair configuration for the Amazon ECS Managed Instances capacity provider. Indicates whether Amazon ECS automatically replaces container instances that are detected as unhealthy.</p>"""
