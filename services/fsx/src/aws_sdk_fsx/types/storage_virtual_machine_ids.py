"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.storage_virtual_machine_id

StorageVirtualMachineIds: TypeAlias = list[
    "aws_sdk_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachineIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StorageVirtualMachineIds:
    return list(data)
