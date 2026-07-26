"""Generated from Smithy shape ``com.amazonaws.fsx#CopySnapshotAndUpdateVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.client_request_token
    import capo_fsx.types.open_zfs_copy_strategy
    import capo_fsx.types.resource_arn
    import capo_fsx.types.update_open_zfs_volume_options
    import capo_fsx.types.volume_id


class CopySnapshotAndUpdateVolumeRequest(TypedDict, closed=True):
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    volume_id: NotRequired["capo_fsx.types.volume_id.VolumeId"]
    """<p>Specifies the ID of the volume that you are copying the snapshot to.</p>"""
    source_snapshot_arn: NotRequired["capo_fsx.types.resource_arn.ResourceARN"]
    copy_strategy: NotRequired[
        "capo_fsx.types.open_zfs_copy_strategy.OpenZFSCopyStrategy"
    ]
    """<p>Specifies the strategy to use when copying data from a snapshot to the volume. </p> <ul> <li> <p> <code>FULL_COPY</code> - Copies all data from the snapshot to the volume. </p> </li> <li> <p> <code>INCREMENTAL_COPY</code> - Copies only the snapshot data that's changed since the previous replication.</p> </li> </ul> <note> <p> <code>CLONE</code> isn't a valid copy strategy option for the <code>CopySnapshotAndUpdateVolume</code> operation.</p> </note>"""
    options: NotRequired[
        "capo_fsx.types.update_open_zfs_volume_options.UpdateOpenZFSVolumeOptions"
    ]
    """<p>Confirms that you want to delete data on the destination volume that wasn’t there during the previous snapshot replication.</p> <p>Your replication will fail if you don’t include an option for a specific type of data and that data is on your destination. For example, if you don’t include <code>DELETE_INTERMEDIATE_SNAPSHOTS</code> and there are intermediate snapshots on the destination, you can’t copy the snapshot.</p> <ul> <li> <p> <code>DELETE_INTERMEDIATE_SNAPSHOTS</code> - Deletes snapshots on the destination volume that aren’t on the source volume.</p> </li> <li> <p> <code>DELETE_CLONED_VOLUMES</code> - Deletes snapshot clones on the destination volume that aren't on the source volume.</p> </li> <li> <p> <code>DELETE_INTERMEDIATE_DATA</code> - Overwrites snapshots on the destination volume that don’t match the source snapshot that you’re copying.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopySnapshotAndUpdateVolumeRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "source_snapshot_arn" in value:
        out["SourceSnapshotARN"] = value["source_snapshot_arn"]
    if "copy_strategy" in value:
        import capo_fsx.types.open_zfs_copy_strategy

        out["CopyStrategy"] = (
            capo_fsx.types.open_zfs_copy_strategy.serialize_aws_json_1_1(
                value["copy_strategy"]
            )
        )
    if "options" in value:
        import capo_fsx.types.update_open_zfs_volume_options

        out["Options"] = (
            capo_fsx.types.update_open_zfs_volume_options.serialize_aws_json_1_1(
                value["options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopySnapshotAndUpdateVolumeRequest:
    out: CopySnapshotAndUpdateVolumeRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "SourceSnapshotARN" in data:
        out["source_snapshot_arn"] = data["SourceSnapshotARN"]
    if "CopyStrategy" in data:
        import capo_fsx.types.open_zfs_copy_strategy

        out["copy_strategy"] = (
            capo_fsx.types.open_zfs_copy_strategy.deserialize_aws_json_1_1(
                data["CopyStrategy"]
            )
        )
    if "Options" in data:
        import capo_fsx.types.update_open_zfs_volume_options

        out["options"] = (
            capo_fsx.types.update_open_zfs_volume_options.deserialize_aws_json_1_1(
                data["Options"]
            )
        )
    return out
