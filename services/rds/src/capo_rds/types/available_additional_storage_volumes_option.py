"""Generated from Smithy shape ``com.amazonaws.rds#AvailableAdditionalStorageVolumesOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.double_optional
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class AvailableAdditionalStorageVolumesOption(TypedDict, closed=True):
    supports_storage_autoscaling: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the additional storage volume supports storage autoscaling.</p>"""
    supports_storage_throughput: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the additional storage volume supports configurable storage throughput.</p>"""
    supports_iops: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>Indicates whether the additional storage volume supports provisioned IOPS.</p>"""
    storage_type: NotRequired["capo_rds.types.string.String"]
    """<p>The storage type for the additional storage volume.</p> <p>Valid Values: <code>GP3 | IO2</code> </p>"""
    min_storage_size: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The minimum amount of storage that you can allocate for the additional storage volume, in gibibytes (GiB).</p>"""
    max_storage_size: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum amount of storage that you can allocate for the additional storage volume, in gibibytes (GiB).</p>"""
    min_iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The minimum number of I/O operations per second (IOPS) that the additional storage volume supports.</p>"""
    max_iops: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of I/O operations per second (IOPS) that the additional storage volume supports.</p>"""
    min_iops_per_gib: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>The minimum ratio of I/O operations per second (IOPS) to gibibytes (GiB) of storage for the additional storage volume.</p>"""
    max_iops_per_gib: NotRequired["capo_rds.types.double_optional.DoubleOptional"]
    """<p>The maximum ratio of I/O operations per second (IOPS) to gibibytes (GiB) of storage for the additional storage volume.</p>"""
    min_storage_throughput: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The minimum storage throughput that the additional storage volume supports, in mebibytes per second (MiBps).</p>"""
    max_storage_throughput: NotRequired[
        "capo_rds.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum storage throughput that the additional storage volume supports, in mebibytes per second (MiBps).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailableAdditionalStorageVolumesOption,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "supports_storage_autoscaling" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsStorageAutoscaling",
                "true" if value["supports_storage_autoscaling"] else "false",
            )
        )
    if "supports_storage_throughput" in value:
        pairs.append(
            (
                f"{key_prefix}SupportsStorageThroughput",
                "true" if value["supports_storage_throughput"] else "false",
            )
        )
    if "supports_iops" in value:
        pairs.append(
            (f"{key_prefix}SupportsIops", "true" if value["supports_iops"] else "false")
        )
    if "storage_type" in value:
        pairs.append((f"{key_prefix}StorageType", str(value["storage_type"])))
    if "min_storage_size" in value:
        pairs.append((f"{key_prefix}MinStorageSize", str(value["min_storage_size"])))
    if "max_storage_size" in value:
        pairs.append((f"{key_prefix}MaxStorageSize", str(value["max_storage_size"])))
    if "min_iops" in value:
        pairs.append((f"{key_prefix}MinIops", str(value["min_iops"])))
    if "max_iops" in value:
        pairs.append((f"{key_prefix}MaxIops", str(value["max_iops"])))
    if "min_iops_per_gib" in value:
        pairs.append(
            (
                f"{key_prefix}MinIopsPerGib",
                (
                    "NaN"
                    if value["min_iops_per_gib"] != value["min_iops_per_gib"]
                    else "Infinity"
                    if value["min_iops_per_gib"] == float("inf")
                    else "-Infinity"
                    if value["min_iops_per_gib"] == float("-inf")
                    else str(value["min_iops_per_gib"])
                ),
            )
        )
    if "max_iops_per_gib" in value:
        pairs.append(
            (
                f"{key_prefix}MaxIopsPerGib",
                (
                    "NaN"
                    if value["max_iops_per_gib"] != value["max_iops_per_gib"]
                    else "Infinity"
                    if value["max_iops_per_gib"] == float("inf")
                    else "-Infinity"
                    if value["max_iops_per_gib"] == float("-inf")
                    else str(value["max_iops_per_gib"])
                ),
            )
        )
    if "min_storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}MinStorageThroughput", str(value["min_storage_throughput"]))
        )
    if "max_storage_throughput" in value:
        pairs.append(
            (f"{key_prefix}MaxStorageThroughput", str(value["max_storage_throughput"]))
        )


def deserialize_query(el: Element) -> AvailableAdditionalStorageVolumesOption:
    out: AvailableAdditionalStorageVolumesOption = {}  # type: ignore[typeddict-item]
    child_supports_storage_autoscaling = el.find("SupportsStorageAutoscaling")
    if child_supports_storage_autoscaling is not None:
        out["supports_storage_autoscaling"] = (
            child_supports_storage_autoscaling.text or ""
        ).lower() == "true"
    child_supports_storage_throughput = el.find("SupportsStorageThroughput")
    if child_supports_storage_throughput is not None:
        out["supports_storage_throughput"] = (
            child_supports_storage_throughput.text or ""
        ).lower() == "true"
    child_supports_iops = el.find("SupportsIops")
    if child_supports_iops is not None:
        out["supports_iops"] = (child_supports_iops.text or "").lower() == "true"
    child_storage_type = el.find("StorageType")
    if child_storage_type is not None:
        out["storage_type"] = str(child_storage_type.text or "")
    child_min_storage_size = el.find("MinStorageSize")
    if child_min_storage_size is not None:
        out["min_storage_size"] = int(child_min_storage_size.text or "")
    child_max_storage_size = el.find("MaxStorageSize")
    if child_max_storage_size is not None:
        out["max_storage_size"] = int(child_max_storage_size.text or "")
    child_min_iops = el.find("MinIops")
    if child_min_iops is not None:
        out["min_iops"] = int(child_min_iops.text or "")
    child_max_iops = el.find("MaxIops")
    if child_max_iops is not None:
        out["max_iops"] = int(child_max_iops.text or "")
    child_min_iops_per_gib = el.find("MinIopsPerGib")
    if child_min_iops_per_gib is not None:
        out["min_iops_per_gib"] = float(child_min_iops_per_gib.text or "")
    child_max_iops_per_gib = el.find("MaxIopsPerGib")
    if child_max_iops_per_gib is not None:
        out["max_iops_per_gib"] = float(child_max_iops_per_gib.text or "")
    child_min_storage_throughput = el.find("MinStorageThroughput")
    if child_min_storage_throughput is not None:
        out["min_storage_throughput"] = int(child_min_storage_throughput.text or "")
    child_max_storage_throughput = el.find("MaxStorageThroughput")
    if child_max_storage_throughput is not None:
        out["max_storage_throughput"] = int(child_max_storage_throughput.text or "")
    return out
