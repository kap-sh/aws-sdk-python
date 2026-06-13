"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#RdsDbInstanceStorageConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RdsDbInstanceStorageConfiguration(TypedDict):
    storage_type: NotRequired["str"]
    """<p>The storage type to associate with the DB instance.</p>"""
    allocated_storage_in_gb: NotRequired["float"]
    """<p>The new amount of storage in GB to allocate for the DB instance.</p>"""
    iops: NotRequired["float"]
    """<p>The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for the DB instance.</p>"""
    storage_throughput: NotRequired["float"]
    """<p>The storage throughput for the DB instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RdsDbInstanceStorageConfiguration) -> dict:
    out: dict = {}
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    if "allocated_storage_in_gb" in value:
        out["allocatedStorageInGb"] = value["allocated_storage_in_gb"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "storage_throughput" in value:
        out["storageThroughput"] = value["storage_throughput"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RdsDbInstanceStorageConfiguration:
    out: RdsDbInstanceStorageConfiguration = {}  # type: ignore[typeddict-item]
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    if "allocatedStorageInGb" in data:
        out["allocated_storage_in_gb"] = data["allocatedStorageInGb"]
    if "iops" in data:
        out["iops"] = data["iops"]
    if "storageThroughput" in data:
        out["storage_throughput"] = data["storageThroughput"]
    return out
