"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeRecoveryPointInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.tape_arn
    import aws_sdk_storage_gateway.types.tape_recovery_point_status
    import aws_sdk_storage_gateway.types.tape_size
    import aws_sdk_storage_gateway.types.time


class TapeRecoveryPointInfo(TypedDict):
    tape_arn: NotRequired["aws_sdk_storage_gateway.types.tape_arn.TapeARN"]
    """<p>The Amazon Resource Name (ARN) of the virtual tape.</p>"""
    tape_recovery_point_time: NotRequired["aws_sdk_storage_gateway.types.time.Time"]
    """<p>The time when the point-in-time view of the virtual tape was replicated for later recovery.</p> <p>The default timestamp format of the tape recovery point time is in the ISO8601 extended YYYY-MM-DD'T'HH:MM:SS'Z' format.</p>"""
    tape_size_in_bytes: NotRequired["aws_sdk_storage_gateway.types.tape_size.TapeSize"]
    """<p>The size, in bytes, of the virtual tapes to recover.</p>"""
    tape_status: NotRequired[
        "aws_sdk_storage_gateway.types.tape_recovery_point_status.TapeRecoveryPointStatus"
    ]
    """<p>The status of the virtual tapes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TapeRecoveryPointInfo) -> dict:
    out: dict = {}
    if "tape_arn" in value:
        out["TapeARN"] = value["tape_arn"]
    if "tape_recovery_point_time" in value:
        import aws_sdk_storage_gateway.types.time

        out["TapeRecoveryPointTime"] = (
            aws_sdk_storage_gateway.types.time.serialize_aws_json_1_1(
                value["tape_recovery_point_time"]
            )
        )
    if "tape_size_in_bytes" in value:
        out["TapeSizeInBytes"] = value["tape_size_in_bytes"]
    if "tape_status" in value:
        out["TapeStatus"] = value["tape_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TapeRecoveryPointInfo:
    out: TapeRecoveryPointInfo = {}  # type: ignore[typeddict-item]
    if "TapeARN" in data:
        out["tape_arn"] = data["TapeARN"]
    if "TapeRecoveryPointTime" in data:
        import aws_sdk_storage_gateway.types.time

        out["tape_recovery_point_time"] = (
            aws_sdk_storage_gateway.types.time.deserialize_aws_json_1_1(
                data["TapeRecoveryPointTime"]
            )
        )
    if "TapeSizeInBytes" in data:
        out["tape_size_in_bytes"] = data["TapeSizeInBytes"]
    if "TapeStatus" in data:
        out["tape_status"] = data["TapeStatus"]
    return out
