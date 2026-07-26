"""Generated from Smithy shape ``com.amazonaws.ecs#DevicesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.device

DevicesList: TypeAlias = list["capo_ecs.types.device.Device"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevicesList) -> list:
    import capo_ecs.types.device

    out: list = []
    for item in value:
        out.append(capo_ecs.types.device.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DevicesList:
    import capo_ecs.types.device

    out: DevicesList = []
    for item in data:
        out.append(capo_ecs.types.device.deserialize_aws_json_1_1(item))
    return out
