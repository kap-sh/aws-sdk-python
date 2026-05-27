"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateCapacityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_scaling_group_provider_update
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.update_managed_instances_provider_configuration


class UpdateCapacityProviderRequest(TypedDict):
    name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the capacity provider to update.</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the cluster that contains the capacity provider to update. Managed instances capacity providers are cluster-scoped and can only be updated within their associated cluster.</p>"""
    auto_scaling_group_provider: NotRequired[
        "aws_sdk_ecs.types.auto_scaling_group_provider_update.AutoScalingGroupProviderUpdate"
    ]
    """<p>An object that represent the parameters to update for the Auto Scaling group capacity provider.</p>"""
    managed_instances_provider: NotRequired[
        "aws_sdk_ecs.types.update_managed_instances_provider_configuration.UpdateManagedInstancesProviderConfiguration"
    ]
    """<p>The updated configuration for the Amazon ECS Managed Instances provider. You can modify the infrastructure role, instance launch template, and tag propagation settings. Changes take effect for new instances launched after the update.</p>"""
