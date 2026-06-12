"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachineFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.storage_virtual_machine_filter

StorageVirtualMachineFilters: TypeAlias = list[
    "aws_sdk_fsx.types.storage_virtual_machine_filter.StorageVirtualMachineFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachineFilters) -> list:
    import aws_sdk_fsx.types.storage_virtual_machine_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_fsx.types.storage_virtual_machine_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StorageVirtualMachineFilters:
    import aws_sdk_fsx.types.storage_virtual_machine_filter

    out: StorageVirtualMachineFilters = []
    for item in data:
        out.append(
            aws_sdk_fsx.types.storage_virtual_machine_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
