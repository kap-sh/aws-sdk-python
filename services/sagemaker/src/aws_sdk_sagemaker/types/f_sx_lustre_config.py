"""Generated from Smithy shape ``com.amazonaws.sagemaker#FSxLustreConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.f_sx_lustre_per_unit_storage_throughput
    import aws_sdk_sagemaker.types.f_sx_lustre_size_in_gi_b


class FSxLustreConfig(TypedDict):
    size_in_gi_b: NotRequired[
        "aws_sdk_sagemaker.types.f_sx_lustre_size_in_gi_b.FSxLustreSizeInGiB"
    ]
    """<p>The storage capacity of the Amazon FSx for Lustre file system, specified in gibibytes (GiB).</p>"""
    per_unit_storage_throughput: NotRequired[
        "aws_sdk_sagemaker.types.f_sx_lustre_per_unit_storage_throughput.FSxLustrePerUnitStorageThroughput"
    ]
    """<p>The throughput capacity of the Amazon FSx for Lustre file system, measured in MB/s per TiB of storage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FSxLustreConfig) -> dict:
    out: dict = {}
    if "size_in_gi_b" in value:
        out["SizeInGiB"] = value["size_in_gi_b"]
    if "per_unit_storage_throughput" in value:
        out["PerUnitStorageThroughput"] = value["per_unit_storage_throughput"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FSxLustreConfig:
    out: FSxLustreConfig = {}  # type: ignore[typeddict-item]
    if "SizeInGiB" in data:
        out["size_in_gi_b"] = data["SizeInGiB"]
    if "PerUnitStorageThroughput" in data:
        out["per_unit_storage_throughput"] = data["PerUnitStorageThroughput"]
    return out
