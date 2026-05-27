"""Generated from Smithy shape ``com.amazonaws.ecs#CreateCapacityProviderRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.auto_scaling_group_provider
    import aws_sdk_ecs.types.create_managed_instances_provider_configuration
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags


class CreateCapacityProviderRequest(TypedDict):
    name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the capacity provider. Up to 255 characters are allowed. They include letters (both upper and lowercase letters), numbers, underscores (_), and hyphens (-). The name can't be prefixed with \"<code>aws</code>\", \"<code>ecs</code>\", or \"<code>fargate</code>\".</p>"""
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the cluster to associate with the capacity provider. When you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.</p>"""
    auto_scaling_group_provider: NotRequired[
        "aws_sdk_ecs.types.auto_scaling_group_provider.AutoScalingGroupProvider"
    ]
    """<p>The details of the Auto Scaling group for the capacity provider.</p>"""
    managed_instances_provider: NotRequired[
        "aws_sdk_ecs.types.create_managed_instances_provider_configuration.CreateManagedInstancesProviderConfiguration"
    ]
    """<p>The configuration for the Amazon ECS Managed Instances provider. This configuration specifies how Amazon ECS manages Amazon EC2 instances on your behalf, including the infrastructure role, instance launch template, and tag propagation settings.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the capacity provider to categorize and organize them more conveniently. Each tag consists of a key and an optional value. You define both of them.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
