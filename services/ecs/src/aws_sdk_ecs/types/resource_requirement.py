"""Generated from Smithy shape ``com.amazonaws.ecs#ResourceRequirement``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.resource_type
    import aws_sdk_ecs.types.string


class ResourceRequirement(TypedDict):
    value: "aws_sdk_ecs.types.string.String"
    """<p>The value for the specified resource type.</p> <p>When the type is <code>GPU</code>, the value is the number of physical <code>GPUs</code> the Amazon ECS container agent reserves for the container. The number of GPUs that's reserved for all containers in a task can't exceed the number of available GPUs on the container instance that the task is launched on. You can also specify <code>ALL</code> to allocate all available GPUs on the instance to the container.</p> <p>When the type is <code>NeuronDevice</code>, the value must be <code>ALL</code>. This allocates all available Neuron devices on the instance to the container. Only one container in a task can specify <code>NeuronDevice</code> resources. This resource type is only supported on Managed Instances.</p> <p>When the type is <code>InferenceAccelerator</code>, the <code>value</code> matches the <code>deviceName</code> for an <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_InferenceAccelerator.html\">InferenceAccelerator</a> specified in a task definition.</p>"""
    type: "aws_sdk_ecs.types.resource_type.ResourceType"
    """<p>The type of resource to assign to a container. </p>"""
