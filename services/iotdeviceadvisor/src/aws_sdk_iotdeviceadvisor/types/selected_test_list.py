"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#SelectedTestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.uuid

SelectedTestList: TypeAlias = list["aws_sdk_iotdeviceadvisor.types.uuid.UUID"]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedTestList) -> list:
    return list(value)


def deserialize_json(data: list) -> SelectedTestList:
    return list(data)
