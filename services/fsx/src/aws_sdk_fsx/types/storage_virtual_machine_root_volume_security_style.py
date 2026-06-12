"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineRootVolumeSecurityStyle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

StorageVirtualMachineRootVolumeSecurityStyle: TypeAlias = Literal[
    "UNIX",
    "NTFS",
    "MIXED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNIX",
        "NTFS",
        "MIXED",
    )
)


def serialize_aws_json_1_1(value: StorageVirtualMachineRootVolumeSecurityStyle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageVirtualMachineRootVolumeSecurityStyle:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StorageVirtualMachineRootVolumeSecurityStyle value: {data!r}"
        )
    return cast(StorageVirtualMachineRootVolumeSecurityStyle, data)
