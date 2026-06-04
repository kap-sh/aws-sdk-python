"""Generated from Smithy shape ``com.amazonaws.ecs#NeuronDeviceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string

NeuronDeviceIds: TypeAlias = list["aws_sdk_ecs.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NeuronDeviceIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NeuronDeviceIds:
    return list(data)
