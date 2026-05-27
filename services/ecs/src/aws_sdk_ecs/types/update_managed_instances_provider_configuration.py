"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateManagedInstancesProviderConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_repair_configuration
    import aws_sdk_ecs.types.infrastructure_optimization
    import aws_sdk_ecs.types.instance_launch_template_update
    import aws_sdk_ecs.types.propagate_mi_tags
    import aws_sdk_ecs.types.string


class UpdateManagedInstancesProviderConfiguration(TypedDict):
    infrastructure_role_arn: "aws_sdk_ecs.types.string.String"
    """<p>The updated Amazon Resource Name (ARN) of the infrastructure role. The new role must have the necessary permissions to manage instances and access required Amazon Web Services services.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html\">Amazon ECS infrastructure IAM role</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    instance_launch_template: (
        "aws_sdk_ecs.types.instance_launch_template_update.InstanceLaunchTemplateUpdate"
    )
    """<p>The updated launch template configuration. Changes to the launch template affect new instances launched after the update, while existing instances continue to use their original configuration.</p>"""
    propagate_tags: NotRequired["aws_sdk_ecs.types.propagate_mi_tags.PropagateMITags"]
    """<p>The updated tag propagation setting. When changed, this affects only new instances launched after the update.</p>"""
    infrastructure_optimization: NotRequired[
        "aws_sdk_ecs.types.infrastructure_optimization.InfrastructureOptimization"
    ]
    """<p>The updated infrastructure optimization configuration. Changes to this setting affect how Amazon ECS optimizes instances going forward.</p>"""
    auto_repair_configuration: NotRequired[
        "aws_sdk_ecs.types.auto_repair_configuration.AutoRepairConfiguration"
    ]
    """<p>The updated auto repair configuration for the Amazon ECS Managed Instances capacity provider.</p>"""
