"""Generated from Smithy shape ``com.amazonaws.rds#AdditionalStorageVolumeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.integer
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class AdditionalStorageVolumeOutput(TypedDict, closed=True):
    volume_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the additional storage volume.</p>"""
    storage_volume_status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the additional storage volume.</p> <p>Valid Values: <code>ACTIVE | CREATING | DELETING | MODIFYING | NOT-IN-USE | STORAGE-OPTIMIZATION | VOLUME-FULL</code> </p>"""
    storage_operation_status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of an in-progress storage operation on the additional storage volume. This field appears only while a storage operation is in progress. It isn't present when no storage operation is active. Possible values:</p> <ul> <li> <p> <code>Initializing</code> - The volume is initializing from a snapshot, such as during a snapshot restore, point-in-time restore, read replica creation, or blue/green deployment. Performance can be lower than provisioned until initialization completes.</p> </li> <li> <p> <code>Optimizing</code> - The volume is optimizing following a storage scaling or modification operation.</p> </li> </ul>"""
    storage_operation_percent_progress: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The percentage of the in-progress storage operation on the additional storage volume that has completed, from <code>0</code> to <code>100</code>. This field appears only while a storage operation is in progress. It isn't present when no storage operation is active.</p>"""
    allocated_storage: NotRequired["capo_rds.types.integer.Integer"]
    """<p>The amount of storage allocated for the additional storage volume, in gibibytes (GiB). The minimum is 20 GiB. The maximum is 65,536 GiB (64 TiB).</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The number of I/O operations per second (IOPS) provisioned for the additional storage volume.</p>"""
    max_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which RDS can automatically scale the storage of the additional storage volume.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput value for the additional storage volume, in mebibytes per second (MiBps).</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type for the additional storage volume.</p> <p>Valid Values: <code>GP3 | IO2</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AdditionalStorageVolumeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "volume_name" in value:
        pairs.append((f"{key_prefix}VolumeName", str(value["volume_name"])))
    if "storage_volume_status" in value:
        pairs.append(
            (f"{key_prefix}StorageVolumeStatus", str(value["storage_volume_status"]))
        )
    if "storage_operation_status" in value:
        pairs.append(
            (
                f"{key_prefix}StorageOperationStatus",
                str(value["storage_operation_status"]),
            )
        )
    if "storage_operation_percent_progress" in value:
        pairs.append(
            (
                f"{key_prefix}StorageOperationPercentProgress",
                str(value["storage_operation_percent_progress"]),
            )
        )
    if "allocated_storage" in value:
        pairs.append((f"{key_prefix}AllocatedStorage", str(value["allocated_storage"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}IOPS", str(value["iops"])))
    if "max_allocated_storage" in value:
        pairs.append(
            (f"{key_prefix}MaxAllocatedStorage", str(value["max_allocated_storage"]))
        )
    if "storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}StorageThroughput", str(value["storage_throughput"]))
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))


def deserialize_query(el: Element) -> AdditionalStorageVolumeOutput:
    out: AdditionalStorageVolumeOutput = {}  # type: ignore[typeddict-item]
    child_volume_name = el.find("VolumeName")
    if child_volume_name is not None:
        out["volume_name"] = str(child_volume_name.text or "")
    child_storage_volume_status = el.find("StorageVolumeStatus")
    if child_storage_volume_status is not None:
        out["storage_volume_status"] = str(child_storage_volume_status.text or "")
    child_storage_operation_status = el.find("StorageOperationStatus")
    if child_storage_operation_status is not None:
        out["storage_operation_status"] = str(child_storage_operation_status.text or "")
    child_storage_operation_percent_progress = el.find(
        "StorageOperationPercentProgress"
    )
    if child_storage_operation_percent_progress is not None:
        out["storage_operation_percent_progress"] = int(
            child_storage_operation_percent_progress.text or ""
        )
    child_allocated_storage = el.find("AllocatedStorage")
    if child_allocated_storage is not None:
        out["allocated_storage"] = int(child_allocated_storage.text or "")
    child_iops = el.find("IOPS")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_max_allocated_storage = el.find("MaxAllocatedStorage")
    if child_max_allocated_storage is not None:
        out["max_allocated_storage"] = int(child_max_allocated_storage.text or "")
    child_storage_throughput = el.find("StorageThroughput")
    if child_storage_throughput is not None:
        out["storage_throughput"] = int(child_storage_throughput.text or "")
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    return out
