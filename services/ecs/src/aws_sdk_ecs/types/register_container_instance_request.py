"""Generated from Smithy shape ``com.amazonaws.ecs#RegisterContainerInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes
    import aws_sdk_ecs.types.platform_devices
    import aws_sdk_ecs.types.resources
    import aws_sdk_ecs.types.string
    import aws_sdk_ecs.types.tags
    import aws_sdk_ecs.types.version_info


class RegisterContainerInstanceRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to register your container instance with. If you do not specify a cluster, the default cluster is assumed.</p>"""
    instance_identity_document: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The instance identity document for the EC2 instance to register. This document can be found by running the following command from the instance: <code>curl http://169.254.169.254/latest/dynamic/instance-identity/document/</code> </p>"""
    instance_identity_document_signature: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The instance identity document signature for the EC2 instance to register. This signature can be found by running the following command from the instance: <code>curl http://169.254.169.254/latest/dynamic/instance-identity/signature/</code> </p>"""
    total_resources: NotRequired["aws_sdk_ecs.types.resources.Resources"]
    """<p>The resources available on the instance.</p>"""
    version_info: NotRequired["aws_sdk_ecs.types.version_info.VersionInfo"]
    """<p>The version information for the Amazon ECS container agent and Docker daemon that runs on the container instance.</p>"""
    container_instance_arn: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The ARN of the container instance (if it was previously registered).</p>"""
    attributes: NotRequired["aws_sdk_ecs.types.attributes.Attributes"]
    """<p>The container instance attributes that this container instance supports.</p>"""
    platform_devices: NotRequired["aws_sdk_ecs.types.platform_devices.PlatformDevices"]
    """<p>The devices that are available on the container instance. The supported device types are GPUs and Neuron devices.</p>"""
    tags: NotRequired["aws_sdk_ecs.types.tags.Tags"]
    """<p>The metadata that you apply to the container instance to help you categorize and organize them. Each tag consists of a key and an optional value. You define both.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case-sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for either keys or values as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys or values with this prefix. Tags with this prefix do not count against your tags per resource limit.</p> </li> </ul>"""
