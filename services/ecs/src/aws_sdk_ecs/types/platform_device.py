"""Generated from Smithy shape ``com.amazonaws.ecs#PlatformDevice``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.platform_device_type
    import aws_sdk_ecs.types.string


class PlatformDevice(TypedDict, closed=True):
    id: "aws_sdk_ecs.types.string.String"
    """<p>The ID for the GPU or Neuron device on the container instance. For GPUs, the available GPU IDs can also be obtained on the container instance in the <code>/var/lib/ecs/gpu/nvidia_gpu_info.json</code> file. For Neuron devices, the ID corresponds to the device index (for example, <code>0</code> for <code>/dev/neuron0</code>).</p>"""
    type: "aws_sdk_ecs.types.platform_device_type.PlatformDeviceType"
    """<p>The type of device that's available on the container instance. The supported values are <code>GPU</code> and <code>NEURON_DEVICE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformDevice) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_ecs.types.platform_device_type

    out["type"] = aws_sdk_ecs.types.platform_device_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PlatformDevice:
    out: PlatformDevice = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PlatformDevice.id required")
    if "type" in data:
        import aws_sdk_ecs.types.platform_device_type

        out["type"] = aws_sdk_ecs.types.platform_device_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("PlatformDevice.type required")
    return out
