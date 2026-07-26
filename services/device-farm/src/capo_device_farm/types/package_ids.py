"""Generated from Smithy shape ``com.amazonaws.devicefarm#PackageIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.string

PackageIds: TypeAlias = list["capo_device_farm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PackageIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PackageIds:
    return list(data)
