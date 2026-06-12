"""Generated from Smithy shape ``com.amazonaws.fsx#CopySnapshotAndUpdateVolumeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.administrative_actions
    import aws_sdk_fsx.types.volume_id
    import aws_sdk_fsx.types.volume_lifecycle


class CopySnapshotAndUpdateVolumeResponse(TypedDict):
    volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume that you copied the snapshot to.</p>"""
    lifecycle: NotRequired["aws_sdk_fsx.types.volume_lifecycle.VolumeLifecycle"]
    """<p>The lifecycle state of the destination volume. </p>"""
    administrative_actions: NotRequired[
        "aws_sdk_fsx.types.administrative_actions.AdministrativeActions"
    ]
    """<p>A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopySnapshotAndUpdateVolumeResponse) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.volume_lifecycle

        out["Lifecycle"] = aws_sdk_fsx.types.volume_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "administrative_actions" in value:
        import aws_sdk_fsx.types.administrative_actions

        out["AdministrativeActions"] = (
            aws_sdk_fsx.types.administrative_actions.serialize_aws_json_1_1(
                value["administrative_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopySnapshotAndUpdateVolumeResponse:
    out: CopySnapshotAndUpdateVolumeResponse = {}  # type: ignore[typeddict-item]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.volume_lifecycle

        out["lifecycle"] = aws_sdk_fsx.types.volume_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if "AdministrativeActions" in data:
        import aws_sdk_fsx.types.administrative_actions

        out["administrative_actions"] = (
            aws_sdk_fsx.types.administrative_actions.deserialize_aws_json_1_1(
                data["AdministrativeActions"]
            )
        )
    return out
