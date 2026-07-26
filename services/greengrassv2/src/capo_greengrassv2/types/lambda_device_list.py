"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaDeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.lambda_device_mount

LambdaDeviceList: TypeAlias = list[
    "capo_greengrassv2.types.lambda_device_mount.LambdaDeviceMount"
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaDeviceList) -> list:
    import capo_greengrassv2.types.lambda_device_mount

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.lambda_device_mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> LambdaDeviceList:
    import capo_greengrassv2.types.lambda_device_mount

    out: LambdaDeviceList = []
    for item in data:
        out.append(capo_greengrassv2.types.lambda_device_mount.deserialize_json(item))
    return out
