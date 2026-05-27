"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProvider``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_scaling_group_provider
    import aws_sdk_ecs.types.capacity_provider_status
    import aws_sdk_ecs.types.capacity_provider_type
    import aws_sdk_ecs.types.capacity_provider_update_status
    import aws_sdk_ecs.types.managed_instances_provider
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags


class CapacityProvider(TypedDict):
    capacity_provider_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the capacity provider.</p>"""
    name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the capacity provider.</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The cluster that this capacity provider is associated with. Managed instances capacity providers are cluster-scoped, meaning they can only be used within their associated cluster.</p> <p>This is required for Managed instances.</p>"""
    status: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_status.CapacityProviderStatus"
    ]
    """<p>The current status of the capacity provider. Only capacity providers in an <code>ACTIVE</code> state can be used in a cluster. When a capacity provider is successfully deleted, it has an <code>INACTIVE</code> status.</p>"""
    auto_scaling_group_provider: NotRequired[
        "aws_sdk_ecs.types.auto_scaling_group_provider.AutoScalingGroupProvider"
    ]
    """<p>The Auto Scaling group settings for the capacity provider.</p>"""
    managed_instances_provider: NotRequired[
        "aws_sdk_ecs.types.managed_instances_provider.ManagedInstancesProvider"
    ]
    """<p>The configuration for the Amazon ECS Managed Instances provider. This includes the infrastructure role, the launch template configuration, and tag propagation settings.</p>"""
    update_status: NotRequired[
        "aws_sdk_ecs.types.capacity_provider_update_status.CapacityProviderUpdateStatus"
    ]
    """<p>The update status of the capacity provider. The following are the possible states that is returned.</p> <dl> <dt>DELETE_IN_PROGRESS</dt> <dd> <p>The capacity provider is in the process of being deleted.</p> </dd> <dt>DELETE_COMPLETE</dt> <dd> <p>The capacity provider was successfully deleted and has an <code>INACTIVE</code> status.</p> </dd> <dt>DELETE_FAILED</dt> <dd> <p>The capacity provider can't be deleted. The update status reason provides further details about why the delete failed.</p> </dd> </dl>"""
    update_status_reason: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The update status reason. This provides further details about the update status for the capacity provider.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the capacity provider to help you categorize and organize it. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
    type: NotRequired["aws_sdk_ecs.types.capacity_provider_type.CapacityProviderType"]
    """<p>The type of capacity provider. For Amazon ECS Managed Instances, this value is <code>MANAGED_INSTANCES</code>, indicating that Amazon ECS manages the underlying Amazon EC2 instances on your behalf.</p>"""
