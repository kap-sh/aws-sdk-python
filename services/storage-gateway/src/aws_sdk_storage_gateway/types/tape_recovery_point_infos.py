"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeRecoveryPointInfos``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.tape_recovery_point_info

TapeRecoveryPointInfos: TypeAlias = list[
    "aws_sdk_storage_gateway.types.tape_recovery_point_info.TapeRecoveryPointInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeRecoveryPointInfos) -> list:
    import aws_sdk_storage_gateway.types.tape_recovery_point_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.tape_recovery_point_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TapeRecoveryPointInfos:
    import aws_sdk_storage_gateway.types.tape_recovery_point_info

    out: TapeRecoveryPointInfos = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.tape_recovery_point_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
