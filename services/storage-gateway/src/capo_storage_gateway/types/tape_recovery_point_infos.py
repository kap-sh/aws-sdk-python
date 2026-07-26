"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeRecoveryPointInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_storage_gateway.types.tape_recovery_point_info

TapeRecoveryPointInfos: TypeAlias = list[
    "capo_storage_gateway.types.tape_recovery_point_info.TapeRecoveryPointInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeRecoveryPointInfos) -> list:
    import capo_storage_gateway.types.tape_recovery_point_info

    out: list = []
    for item in value:
        out.append(
            capo_storage_gateway.types.tape_recovery_point_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TapeRecoveryPointInfos:
    import capo_storage_gateway.types.tape_recovery_point_info

    out: TapeRecoveryPointInfos = []
    for item in data:
        out.append(
            capo_storage_gateway.types.tape_recovery_point_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
