"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaVolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.lambda_volume_mount

LambdaVolumeList: TypeAlias = list[
    "aws_sdk_greengrassv2.types.lambda_volume_mount.LambdaVolumeMount"
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaVolumeList) -> list:
    import aws_sdk_greengrassv2.types.lambda_volume_mount

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrassv2.types.lambda_volume_mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> LambdaVolumeList:
    import aws_sdk_greengrassv2.types.lambda_volume_mount

    out: LambdaVolumeList = []
    for item in data:
        out.append(
            aws_sdk_greengrassv2.types.lambda_volume_mount.deserialize_json(item)
        )
    return out
