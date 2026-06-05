"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStorageInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disk_info_list
    import aws_sdk_ec2.types.disk_size
    import aws_sdk_ec2.types.ephemeral_nvme_support
    import aws_sdk_ec2.types.instance_storage_encryption_support


class InstanceStorageInfo(TypedDict):
    total_size_in_gb: NotRequired["aws_sdk_ec2.types.disk_size.DiskSize"]
    """<p>The total size of the disks, in GB.</p>"""
    disks: NotRequired["aws_sdk_ec2.types.disk_info_list.DiskInfoList"]
    """<p>Describes the disks that are available for the instance type.</p>"""
    nvme_support: NotRequired[
        "aws_sdk_ec2.types.ephemeral_nvme_support.EphemeralNvmeSupport"
    ]
    """<p>Indicates whether non-volatile memory express (NVMe) is supported.</p>"""
    encryption_support: NotRequired[
        "aws_sdk_ec2.types.instance_storage_encryption_support.InstanceStorageEncryptionSupport"
    ]
    """<p>Indicates whether data is encrypted at rest.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceStorageInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "total_size_in_gb" in value:
        pairs.append((f"{prefix}.TotalSizeInGB", str(value["total_size_in_gb"])))
    if "disks" in value:
        import aws_sdk_ec2.types.disk_info_list

        aws_sdk_ec2.types.disk_info_list.serialize_ec2_query(
            value["disks"], pairs, f"{prefix}.Disks"
        )
    if "nvme_support" in value:
        import aws_sdk_ec2.types.ephemeral_nvme_support

        aws_sdk_ec2.types.ephemeral_nvme_support.serialize_ec2_query(
            value["nvme_support"], pairs, f"{prefix}.NvmeSupport"
        )
    if "encryption_support" in value:
        import aws_sdk_ec2.types.instance_storage_encryption_support

        aws_sdk_ec2.types.instance_storage_encryption_support.serialize_ec2_query(
            value["encryption_support"], pairs, f"{prefix}.EncryptionSupport"
        )


def deserialize_ec2_query(el: Element) -> InstanceStorageInfo:
    out: InstanceStorageInfo = {}  # type: ignore[typeddict-item]
    child_total_size_in_gb = el.find("TotalSizeInGB")
    if child_total_size_in_gb is not None:
        out["total_size_in_gb"] = int(child_total_size_in_gb.text or "")
    if el.find("Disks") is not None:
        import aws_sdk_ec2.types.disk_info_list

        out["disks"] = aws_sdk_ec2.types.disk_info_list.deserialize_ec2_query(
            el, "Disks"
        )
    child_nvme_support = el.find("NvmeSupport")
    if child_nvme_support is not None:
        import aws_sdk_ec2.types.ephemeral_nvme_support

        out["nvme_support"] = (
            aws_sdk_ec2.types.ephemeral_nvme_support.deserialize_ec2_query(
                child_nvme_support
            )
        )
    child_encryption_support = el.find("EncryptionSupport")
    if child_encryption_support is not None:
        import aws_sdk_ec2.types.instance_storage_encryption_support

        out["encryption_support"] = (
            aws_sdk_ec2.types.instance_storage_encryption_support.deserialize_ec2_query(
                child_encryption_support
            )
        )
    return out
