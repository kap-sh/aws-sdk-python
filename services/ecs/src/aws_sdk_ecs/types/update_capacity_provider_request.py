"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateCapacityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCapacityProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "auto_scaling_group_provider" in value:
        import aws_sdk_ecs.types.auto_scaling_group_provider_update

        out["autoScalingGroupProvider"] = (
            aws_sdk_ecs.types.auto_scaling_group_provider_update.serialize_aws_json_1_1(
                value["auto_scaling_group_provider"]
            )
        )
    if "managed_instances_provider" in value:
        import aws_sdk_ecs.types.update_managed_instances_provider_configuration

        out["managedInstancesProvider"] = (
            aws_sdk_ecs.types.update_managed_instances_provider_configuration.serialize_aws_json_1_1(
                value["managed_instances_provider"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCapacityProviderRequest:
    out: UpdateCapacityProviderRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateCapacityProviderRequest.name required")
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "autoScalingGroupProvider" in data:
        import aws_sdk_ecs.types.auto_scaling_group_provider_update

        out["auto_scaling_group_provider"] = (
            aws_sdk_ecs.types.auto_scaling_group_provider_update.deserialize_aws_json_1_1(
                data["autoScalingGroupProvider"]
            )
        )
    if "managedInstancesProvider" in data:
        import aws_sdk_ecs.types.update_managed_instances_provider_configuration

        out["managed_instances_provider"] = (
            aws_sdk_ecs.types.update_managed_instances_provider_configuration.deserialize_aws_json_1_1(
                data["managedInstancesProvider"]
            )
        )
    return out
