"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerVolumeMounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.eks_container_volume_mount

EksContainerVolumeMounts: TypeAlias = list[
    "aws_sdk_batch.types.eks_container_volume_mount.EksContainerVolumeMount"
]


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerVolumeMounts) -> list:
    import aws_sdk_batch.types.eks_container_volume_mount

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.eks_container_volume_mount.serialize_json(item))
    return out


def deserialize_json(data: list) -> EksContainerVolumeMounts:
    import aws_sdk_batch.types.eks_container_volume_mount

    out: EksContainerVolumeMounts = []
    for item in data:
        out.append(
            aws_sdk_batch.types.eks_container_volume_mount.deserialize_json(item)
        )
    return out
