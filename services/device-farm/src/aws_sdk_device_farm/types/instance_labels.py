"""Generated from Smithy shape ``com.amazonaws.devicefarm#InstanceLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.string

InstanceLabels: TypeAlias = list["aws_sdk_device_farm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceLabels) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InstanceLabels:
    return list(data)
