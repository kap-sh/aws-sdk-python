"""Generated from Smithy shape ``com.amazonaws.sagemaker#Devices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.device

Devices: TypeAlias = list["aws_sdk_sagemaker.types.device.Device"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Devices) -> list:
    import aws_sdk_sagemaker.types.device

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.device.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Devices:
    import aws_sdk_sagemaker.types.device

    out: Devices = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.device.deserialize_aws_json_1_1(item))
    return out
