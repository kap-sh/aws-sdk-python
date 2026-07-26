"""Generated from Smithy shape ``com.amazonaws.greengrassv2#LambdaVolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.lambda_volume_mount

LambdaVolumeList: TypeAlias = list[
    "capo_greengrassv2.types.lambda_volume_mount.LambdaVolumeMount"
]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaVolumeList) -> list:
    import capo_greengrassv2.types.lambda_volume_mount

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.lambda_volume_mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> LambdaVolumeList:
    import capo_greengrassv2.types.lambda_volume_mount

    out: LambdaVolumeList = []
    for item in data:
        out.append(capo_greengrassv2.types.lambda_volume_mount.deserialize_json(item))
    return out
