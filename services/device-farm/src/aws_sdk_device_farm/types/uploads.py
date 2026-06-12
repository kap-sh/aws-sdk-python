"""Generated from Smithy shape ``com.amazonaws.devicefarm#Uploads``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.upload

Uploads: TypeAlias = list["aws_sdk_device_farm.types.upload.Upload"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Uploads) -> list:
    import aws_sdk_device_farm.types.upload

    out: list = []
    for item in value:
        out.append(aws_sdk_device_farm.types.upload.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Uploads:
    import aws_sdk_device_farm.types.upload

    out: Uploads = []
    for item in data:
        out.append(aws_sdk_device_farm.types.upload.deserialize_aws_json_1_1(item))
    return out
