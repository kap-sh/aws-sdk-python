"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteSnapshotScheduleInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.volume_arn


class DeleteSnapshotScheduleInput(TypedDict):
    volume_arn: "aws_sdk_storage_gateway.types.volume_arn.VolumeARN"
    """<p>The volume which snapshot schedule to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotScheduleInput) -> dict:
    out: dict = {}
    out["VolumeARN"] = value["volume_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotScheduleInput:
    out: DeleteSnapshotScheduleInput = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    else:
        raise DeserializationError("DeleteSnapshotScheduleInput.volume_arn required")
    return out
