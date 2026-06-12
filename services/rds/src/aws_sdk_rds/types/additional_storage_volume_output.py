"""Generated from Smithy shape ``com.amazonaws.rds#AdditionalStorageVolumeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.integer
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class AdditionalStorageVolumeOutput(TypedDict):
    volume_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the additional storage volume.</p>"""
    storage_volume_status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The status of the additional storage volume.</p> <p>Valid Values: <code>ACTIVE | CREATING | DELETING | MODIFYING | NOT-IN-USE | STORAGE-OPTIMIZATION | VOLUME-FULL</code> </p>"""
    allocated_storage: NotRequired["aws_sdk_rds.types.integer.Integer"]
    """<p>The amount of storage allocated for the additional storage volume, in gibibytes (GiB). The minimum is 20 GiB. The maximum is 65,536 GiB (64 TiB).</p>"""
    iops: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The number of I/O operations per second (IOPS) provisioned for the additional storage volume.</p>"""
    max_allocated_storage: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which RDS can automatically scale the storage of the additional storage volume.</p>"""
    storage_throughput: NotRequired[
        "aws_sdk_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The storage throughput value for the additional storage volume, in mebibytes per second (MiBps).</p>"""
    storage_type: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The storage type for the additional storage volume.</p> <p>Valid Values: <code>GP3 | IO2</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AdditionalStorageVolumeOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "volume_name" in value:
        pairs.append((f"{prefix}.VolumeName", str(value["volume_name"])))
    if "storage_volume_status" in value:
        pairs.append(
            (f"{prefix}.StorageVolumeStatus", str(value["storage_volume_status"]))
        )
    if "allocated_storage" in value:
        pairs.append((f"{prefix}.AllocatedStorage", str(value["allocated_storage"])))
    if "iops" in value:
        pairs.append((f"{prefix}.IOPS", str(value["iops"])))
    if "max_allocated_storage" in value:
        pairs.append(
            (f"{prefix}.MaxAllocatedStorage", str(value["max_allocated_storage"]))
        )
    if "storage_throughput" in value:
        pairs.append((f"{prefix}.StorageThroughput", str(value["storage_throughput"])))
    if "storage_type" in value:
        pairs.append((f"{prefix}.StorageType", str(value["storage_type"])))


def deserialize_query(el: Element) -> AdditionalStorageVolumeOutput:
    out: AdditionalStorageVolumeOutput = {}  # type: ignore[typeddict-item]
    child_volume_name = el.find("VolumeName")
    if child_volume_name is not None:
        out["volume_name"] = str(child_volume_name.text or "")
    child_storage_volume_status = el.find("StorageVolumeStatus")
    if child_storage_volume_status is not None:
        out["storage_volume_status"] = str(child_storage_volume_status.text or "")
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
