"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#DBStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.allocated_storage
    import aws_sdk_compute_optimizer.types.nullable_iops
    import aws_sdk_compute_optimizer.types.nullable_max_allocated_storage
    import aws_sdk_compute_optimizer.types.nullable_storage_throughput
    import aws_sdk_compute_optimizer.types.storage_type


class DBStorageConfiguration(TypedDict, closed=True):
    storage_type: NotRequired[
        "aws_sdk_compute_optimizer.types.storage_type.StorageType"
    ]
    """<p> The type of DB storage. </p>"""
    allocated_storage: (
        "aws_sdk_compute_optimizer.types.allocated_storage.AllocatedStorage"
    )
    """<p> The size of the DB storage in gigabytes (GB). </p>"""
    iops: NotRequired["aws_sdk_compute_optimizer.types.nullable_iops.NullableIOPS"]
    """<p> The provisioned IOPs of the DB storage. </p>"""
    max_allocated_storage: NotRequired[
        "aws_sdk_compute_optimizer.types.nullable_max_allocated_storage.NullableMaxAllocatedStorage"
    ]
    """<p> The maximum limit in gibibytes (GiB) to which Amazon RDS can automatically scale the storage of the DB instance. </p>"""
    storage_throughput: NotRequired[
        "aws_sdk_compute_optimizer.types.nullable_storage_throughput.NullableStorageThroughput"
    ]
    """<p> The storage throughput of the DB storage. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DBStorageConfiguration) -> dict:
    out: dict = {}
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    out["allocatedStorage"] = value.get("allocated_storage", 0)
    if "iops" in value:
        out["iops"] = value["iops"]
    if "max_allocated_storage" in value:
        out["maxAllocatedStorage"] = value["max_allocated_storage"]
    if "storage_throughput" in value:
        out["storageThroughput"] = value["storage_throughput"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DBStorageConfiguration:
    out: DBStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    if "allocatedStorage" in data:
        out["allocated_storage"] = data["allocatedStorage"]
    else:
        out["allocated_storage"] = 0
    if "iops" in data:
        out["iops"] = data["iops"]
    if "maxAllocatedStorage" in data:
        out["max_allocated_storage"] = data["maxAllocatedStorage"]
    if "storageThroughput" in data:
        out["storage_throughput"] = data["storageThroughput"]
    return out
