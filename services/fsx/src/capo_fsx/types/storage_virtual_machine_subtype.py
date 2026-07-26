"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineSubtype``."""

from typing import Literal, TypeAlias, cast

StorageVirtualMachineSubtype: TypeAlias = Literal[
    "DEFAULT",
    "DP_DESTINATION",
    "SYNC_DESTINATION",
    "SYNC_SOURCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachineSubtype) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageVirtualMachineSubtype:
    return cast(StorageVirtualMachineSubtype, data)
