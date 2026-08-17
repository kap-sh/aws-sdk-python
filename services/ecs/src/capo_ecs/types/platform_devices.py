"""Generated from Smithy shape ``com.amazonaws.ecs#PlatformDevices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.platform_device

PlatformDevices: TypeAlias = list["capo_ecs.types.platform_device.PlatformDevice"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlatformDevices) -> list:
    import capo_ecs.types.platform_device

    out: list = []
    for item in value:
        out.append(capo_ecs.types.platform_device.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlatformDevices:
    import capo_ecs.types.platform_device

    out: PlatformDevices = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.platform_device.deserialize_aws_json_1_1(item))
    return out
