"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterFsxLustreConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_dns_name
    import aws_sdk_sagemaker.types.cluster_fsx_mount_path
    import aws_sdk_sagemaker.types.cluster_mount_name


class ClusterFsxLustreConfig(TypedDict):
    dns_name: "aws_sdk_sagemaker.types.cluster_dns_name.ClusterDnsName"
    """<p>The DNS name of the Amazon FSx for Lustre file system.</p>"""
    mount_name: "aws_sdk_sagemaker.types.cluster_mount_name.ClusterMountName"
    """<p>The mount name of the Amazon FSx for Lustre file system.</p>"""
    mount_path: NotRequired[
        "aws_sdk_sagemaker.types.cluster_fsx_mount_path.ClusterFsxMountPath"
    ]
    """<p>The local path where the Amazon FSx for Lustre file system is mounted on instances.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterFsxLustreConfig) -> dict:
    out: dict = {}
    out["DnsName"] = value["dns_name"]
    out["MountName"] = value["mount_name"]
    if "mount_path" in value:
        out["MountPath"] = value["mount_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterFsxLustreConfig:
    out: ClusterFsxLustreConfig = {}  # type: ignore[typeddict-item]
    if "DnsName" in data:
        out["dns_name"] = data["DnsName"]
    else:
        raise DeserializationError("ClusterFsxLustreConfig.dns_name required")
    if "MountName" in data:
        out["mount_name"] = data["MountName"]
    else:
        raise DeserializationError("ClusterFsxLustreConfig.mount_name required")
    if "MountPath" in data:
        out["mount_path"] = data["MountPath"]
    return out
