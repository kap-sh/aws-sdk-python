"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineRootVolumeSecurityStyle``."""

from typing import Literal, TypeAlias, cast

StorageVirtualMachineRootVolumeSecurityStyle: TypeAlias = Literal[
    "UNIX",
    "NTFS",
    "MIXED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachineRootVolumeSecurityStyle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageVirtualMachineRootVolumeSecurityStyle:
    return cast(StorageVirtualMachineRootVolumeSecurityStyle, data)
