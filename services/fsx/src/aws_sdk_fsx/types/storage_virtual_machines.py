"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.storage_virtual_machine

StorageVirtualMachines: TypeAlias = list[
    "aws_sdk_fsx.types.storage_virtual_machine.StorageVirtualMachine"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachines) -> list:
    import aws_sdk_fsx.types.storage_virtual_machine

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fsx.types.storage_virtual_machine.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StorageVirtualMachines:
    import aws_sdk_fsx.types.storage_virtual_machine

    out: StorageVirtualMachines = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.storage_virtual_machine.deserialize_aws_json_1_1(item)
        )
    return out
