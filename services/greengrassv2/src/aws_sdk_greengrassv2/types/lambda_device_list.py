"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaDeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.lambda_device_mount

LambdaDeviceList: TypeAlias = list[
    "aws_sdk_greengrassv2.types.lambda_device_mount.LambdaDeviceMount"
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaDeviceList) -> list:
    import aws_sdk_greengrassv2.types.lambda_device_mount

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrassv2.types.lambda_device_mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> LambdaDeviceList:
    import aws_sdk_greengrassv2.types.lambda_device_mount

    out: LambdaDeviceList = []
    for item in data:
        out.append(
            aws_sdk_greengrassv2.types.lambda_device_mount.deserialize_json(item)
        )
    return out
