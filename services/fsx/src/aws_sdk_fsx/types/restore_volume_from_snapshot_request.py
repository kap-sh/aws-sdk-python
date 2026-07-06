"""Generated from Smithy shape ``com.amazonaws.fsx#RestoreVolumeFromSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.restore_open_zfs_volume_options
    import aws_sdk_fsx.types.snapshot_id
    import aws_sdk_fsx.types.volume_id


class RestoreVolumeFromSnapshotRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    volume_id: NotRequired["aws_sdk_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume that you are restoring.</p>"""
    snapshot_id: NotRequired["aws_sdk_fsx.types.snapshot_id.SnapshotId"]
    """<p>The ID of the source snapshot. Specifies the snapshot that you are restoring from.</p>"""
    options: NotRequired[
        "aws_sdk_fsx.types.restore_open_zfs_volume_options.RestoreOpenZFSVolumeOptions"
    ]
    """<p>The settings used when restoring the specified volume from snapshot.</p> <ul> <li> <p> <code>DELETE_INTERMEDIATE_SNAPSHOTS</code> - Deletes snapshots between the current state and the specified snapshot. If there are intermediate snapshots and this option isn't used, <code>RestoreVolumeFromSnapshot</code> fails.</p> </li> <li> <p> <code>DELETE_CLONED_VOLUMES</code> - Deletes any dependent clone volumes created from intermediate snapshots. If there are any dependent clone volumes and this option isn't used, <code>RestoreVolumeFromSnapshot</code> fails.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreVolumeFromSnapshotRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "options" in value:
        import aws_sdk_fsx.types.restore_open_zfs_volume_options

        out["Options"] = (
            aws_sdk_fsx.types.restore_open_zfs_volume_options.serialize_aws_json_1_1(
                value["options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreVolumeFromSnapshotRequest:
    out: RestoreVolumeFromSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    if "Options" in data:
        import aws_sdk_fsx.types.restore_open_zfs_volume_options

        out["options"] = (
            aws_sdk_fsx.types.restore_open_zfs_volume_options.deserialize_aws_json_1_1(
                data["Options"]
            )
        )
    return out
