"""Generated from Smithy shape ``com.amazonaws.workmail#DeviceModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workmail.types.device_model

DeviceModelList: TypeAlias = list["aws_sdk_workmail.types.device_model.DeviceModel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceModelList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeviceModelList:
    return list(data)
