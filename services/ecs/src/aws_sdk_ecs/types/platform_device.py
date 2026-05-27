"""Generated from Smithy shape ``com.amazonaws.ecs#PlatformDevice``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.platform_device_type
    import aws_sdk_ecs.types.string


class PlatformDevice(TypedDict):
    id: "aws_sdk_ecs.types.string.String"
    """<p>The ID for the GPU or Neuron device on the container instance. For GPUs, the available GPU IDs can also be obtained on the container instance in the <code>/var/lib/ecs/gpu/nvidia_gpu_info.json</code> file. For Neuron devices, the ID corresponds to the device index (for example, <code>0</code> for <code>/dev/neuron0</code>).</p>"""
    type: "aws_sdk_ecs.types.platform_device_type.PlatformDeviceType"
    """<p>The type of device that's available on the container instance. The supported values are <code>GPU</code> and <code>NEURON_DEVICE</code>.</p>"""
