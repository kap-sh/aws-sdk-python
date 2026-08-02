"""Generated from Smithy shape ``com.amazonaws.rds#ModifyAdditionalStorageVolume``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean_optional
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class ModifyAdditionalStorageVolume(TypedDict, closed=True):
    volume_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the additional storage volume that you want to modify.</p> <p>Valid Values: <code>RDSDBDATA2 | RDSDBDATA3 | RDSDBDATA4</code> </p>"""
    allocated_storage: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The amount of storage allocated for the additional storage volume, in gibibytes (GiB). The minimum is 20 GiB. The maximum is 65,536 GiB (64 TiB).</p>"""
    iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The number of I/O operations per second (IOPS) provisioned for the additional storage volume. This setting is only supported for Provisioned IOPS SSD (<code>io1</code> and <code>io2</code>) storage types.</p>"""
    max_allocated_storage: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The upper limit in gibibytes (GiB) to which RDS can automatically scale the storage of the additional storage volume. You must provide a value greater than or equal to <code>AllocatedStorage</code>.</p>"""
    storage_throughput: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The storage throughput value for the additional storage volume, in mebibytes per second (MiBps). This setting applies only to the General Purpose SSD (<code>gp3</code>) storage type.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The new storage type for the additional storage volume.</p> <p>Valid Values: <code>GP3 | IO2</code> </p>"""
    set_for_delete: NotRequired["capo_rds.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether to delete the additional storage volume. The value <code>true</code> schedules the volume for deletion. You can delete an additional storage volume only when it doesn't contain database files or other data.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyAdditionalStorageVolume, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "volume_name" in value:
        pairs.append((f"{key_prefix}VolumeName", str(value["volume_name"])))
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
    if "set_for_delete" in value:
        pairs.append(
            (
                f"{key_prefix}SetForDelete",
                "true" if value["set_for_delete"] else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyAdditionalStorageVolume:
    out: ModifyAdditionalStorageVolume = {}  # type: ignore[typeddict-item]
    child_volume_name = el.find("VolumeName")
    if child_volume_name is not None:
        out["volume_name"] = str(child_volume_name.text or "")
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
    child_set_for_delete = el.find("SetForDelete")
    if child_set_for_delete is not None:
        out["set_for_delete"] = (child_set_for_delete.text or "").lower() == "true"
    return out
