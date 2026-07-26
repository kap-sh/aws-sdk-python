"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.storage_virtual_machine_filter_value

StorageVirtualMachineFilterValues: TypeAlias = list[
    "capo_fsx.types.storage_virtual_machine_filter_value.StorageVirtualMachineFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachineFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StorageVirtualMachineFilterValues:
    return list(data)
