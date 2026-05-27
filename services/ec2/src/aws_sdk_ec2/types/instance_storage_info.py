"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceStorageInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

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
