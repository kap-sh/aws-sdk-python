"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineLifecycle``."""

from typing import Literal, TypeAlias, cast

StorageVirtualMachineLifecycle: TypeAlias = Literal[
    "CREATED",
    "CREATING",
    "DELETING",
    "FAILED",
    "MISCONFIGURED",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachineLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageVirtualMachineLifecycle:
    return cast(StorageVirtualMachineLifecycle, data)
