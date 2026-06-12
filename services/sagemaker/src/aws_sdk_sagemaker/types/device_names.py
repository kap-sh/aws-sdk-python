"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeviceNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.device_name

DeviceNames: TypeAlias = list["aws_sdk_sagemaker.types.device_name.DeviceName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeviceNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeviceNames:
    return list(data)
