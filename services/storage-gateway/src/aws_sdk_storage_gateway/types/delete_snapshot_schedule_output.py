"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteSnapshotScheduleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.volume_arn


class DeleteSnapshotScheduleOutput(TypedDict, closed=True):
    volume_arn: NotRequired["aws_sdk_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The volume which snapshot schedule was deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotScheduleOutput) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotScheduleOutput:
    out: DeleteSnapshotScheduleOutput = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    return out
