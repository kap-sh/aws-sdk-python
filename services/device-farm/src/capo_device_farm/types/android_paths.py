"""Generated from Smithy shape ``com.amazonaws.devicefarm#AndroidPaths``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.string

AndroidPaths: TypeAlias = list["capo_device_farm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AndroidPaths) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AndroidPaths:
    return list(data)
