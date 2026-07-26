"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystemMaintenanceOperations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.file_system_maintenance_operation

FileSystemMaintenanceOperations: TypeAlias = list[
    "capo_fsx.types.file_system_maintenance_operation.FileSystemMaintenanceOperation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemMaintenanceOperations) -> list:
    import capo_fsx.types.file_system_maintenance_operation

    out: list = []
    for item in value:
        out.append(
            capo_fsx.types.file_system_maintenance_operation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FileSystemMaintenanceOperations:
    import capo_fsx.types.file_system_maintenance_operation

    out: FileSystemMaintenanceOperations = []
    for item in data:
        out.append(
            capo_fsx.types.file_system_maintenance_operation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
