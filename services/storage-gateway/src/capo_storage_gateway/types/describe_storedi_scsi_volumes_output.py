"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeStorediSCSIVolumesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.storedi_scsi_volumes


class DescribeStorediSCSIVolumesOutput(TypedDict, closed=True):
    storedi_scsi_volumes: NotRequired[
        "capo_storage_gateway.types.storedi_scsi_volumes.StorediSCSIVolumes"
    ]
    """<p>Describes a single unit of output from <a>DescribeStorediSCSIVolumes</a>. The following fields are returned:</p> <ul> <li> <p> <code>ChapEnabled</code>: Indicates whether mutual CHAP is enabled for the iSCSI target.</p> </li> <li> <p> <code>LunNumber</code>: The logical disk number.</p> </li> <li> <p> <code>NetworkInterfaceId</code>: The network interface ID of the stored volume that initiator use to map the stored volume as an iSCSI target.</p> </li> <li> <p> <code>NetworkInterfacePort</code>: The port used to communicate with iSCSI targets.</p> </li> <li> <p> <code>PreservedExistingData</code>: Indicates when the stored volume was created, existing data on the underlying local disk was preserved.</p> </li> <li> <p> <code>SourceSnapshotId</code>: If the stored volume was created from a snapshot, this field contains the snapshot ID used, e.g. <code>snap-1122aabb</code>. Otherwise, this field is not included.</p> </li> <li> <p> <code>StorediSCSIVolumes</code>: An array of StorediSCSIVolume objects where each object contains metadata about one stored volume.</p> </li> <li> <p> <code>TargetARN</code>: The Amazon Resource Name (ARN) of the volume target.</p> </li> <li> <p> <code>VolumeARN</code>: The Amazon Resource Name (ARN) of the stored volume.</p> </li> <li> <p> <code>VolumeDiskId</code>: The disk ID of the local disk that was specified in the <a>CreateStorediSCSIVolume</a> operation.</p> </li> <li> <p> <code>VolumeId</code>: The unique identifier of the storage volume, e.g. <code>vol-1122AABB</code>.</p> </li> <li> <p> <code>VolumeiSCSIAttributes</code>: An <a>VolumeiSCSIAttributes</a> object that represents a collection of iSCSI attributes for one stored volume.</p> </li> <li> <p> <code>VolumeProgress</code>: Represents the percentage complete if the volume is restoring or bootstrapping that represents the percent of data transferred. This field does not appear in the response if the stored volume is not restoring or bootstrapping.</p> </li> <li> <p> <code>VolumeSizeInBytes</code>: The size of the volume in bytes.</p> </li> <li> <p> <code>VolumeStatus</code>: One of the <code>VolumeStatus</code> values that indicates the state of the volume.</p> </li> <li> <p> <code>VolumeType</code>: One of the enumeration values describing the type of the volume. Currently, only <code>STORED</code> volumes are supported.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStorediSCSIVolumesOutput) -> dict:
    out: dict = {}
    if "storedi_scsi_volumes" in value:
        import capo_storage_gateway.types.storedi_scsi_volumes

        out["StorediSCSIVolumes"] = (
            capo_storage_gateway.types.storedi_scsi_volumes.serialize_aws_json_1_1(
                value["storedi_scsi_volumes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStorediSCSIVolumesOutput:
    out: DescribeStorediSCSIVolumesOutput = {}  # type: ignore[typeddict-item]
    if "StorediSCSIVolumes" in data:
        import capo_storage_gateway.types.storedi_scsi_volumes

        out["storedi_scsi_volumes"] = (
            capo_storage_gateway.types.storedi_scsi_volumes.deserialize_aws_json_1_1(
                data["StorediSCSIVolumes"]
            )
        )
    return out
