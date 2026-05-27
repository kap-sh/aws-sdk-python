"""Generated from Smithy shape ``com.amazonaws.ecs#CreateManagedInstancesProviderConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_repair_configuration
    import aws_sdk_ecs.types.infrastructure_optimization
    import aws_sdk_ecs.types.instance_launch_template
    import aws_sdk_ecs.types.propagate_mi_tags
    import aws_sdk_ecs.types.string


class CreateManagedInstancesProviderConfiguration(TypedDict):
    infrastructure_role_arn: "aws_sdk_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the infrastructure role that Amazon ECS uses to manage instances on your behalf. This role must have permissions to launch, terminate, and manage Amazon EC2 instances, as well as access to other Amazon Web Services services required for Amazon ECS Managed Instances functionality.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html\">Amazon ECS infrastructure IAM role</a> in the <i>Amazon ECS Developer Guide</i>. </p>"""
    instance_launch_template: (
        "aws_sdk_ecs.types.instance_launch_template.InstanceLaunchTemplate"
    )
    """<p>The launch template configuration that specifies how Amazon ECS should launch Amazon EC2 instances. This includes the instance profile, network configuration, storage settings, and instance requirements for attribute-based instance type selection.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html\">Store instance launch parameters in Amazon EC2 launch templates</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    propagate_tags: NotRequired["aws_sdk_ecs.types.propagate_mi_tags.PropagateMITags"]
    """<p>Specifies whether to propagate tags from the capacity provider to the Amazon ECS Managed Instances. When enabled, tags applied to the capacity provider are automatically applied to all instances launched by this provider.</p>"""
    infrastructure_optimization: NotRequired[
        "aws_sdk_ecs.types.infrastructure_optimization.InfrastructureOptimization"
    ]
    """<p>Defines how Amazon ECS Managed Instances optimizes the infrastastructure in your capacity provider. Provides control over the delay between when EC2 instances become idle or underutilized and when Amazon ECS optimizes them.</p>"""
    auto_repair_configuration: NotRequired[
        "aws_sdk_ecs.types.auto_repair_configuration.AutoRepairConfiguration"
    ]
    """<p>The auto repair configuration for the Amazon ECS Managed Instances capacity provider. Use this to enable or disable automatic replacement of container instances that are detected as unhealthy.</p>"""
