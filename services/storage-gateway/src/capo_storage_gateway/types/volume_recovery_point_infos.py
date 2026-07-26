"""Generated from Smithy shape ``com.amazonaws.storagegateway#VolumeRecoveryPointInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.volume_recovery_point_info

VolumeRecoveryPointInfos: TypeAlias = list[
    "capo_storage_gateway.types.volume_recovery_point_info.VolumeRecoveryPointInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeRecoveryPointInfos) -> list:
    import capo_storage_gateway.types.volume_recovery_point_info

    out: list = []
    for item in value:
        out.append(
            capo_storage_gateway.types.volume_recovery_point_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> VolumeRecoveryPointInfos:
    import capo_storage_gateway.types.volume_recovery_point_info

    out: VolumeRecoveryPointInfos = []
    for item in data:
        out.append(
            capo_storage_gateway.types.volume_recovery_point_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
