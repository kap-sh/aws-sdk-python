"""Generated from Smithy shape ``com.amazonaws.backupgateway#VirtualMachines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.virtual_machine

VirtualMachines: TypeAlias = list[
    "aws_sdk_backup_gateway.types.virtual_machine.VirtualMachine"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VirtualMachines) -> list:
    import aws_sdk_backup_gateway.types.virtual_machine

    out: list = []
    for item in value:
        out.append(
            aws_sdk_backup_gateway.types.virtual_machine.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> VirtualMachines:
    import aws_sdk_backup_gateway.types.virtual_machine

    out: VirtualMachines = []
    for item in data:
        out.append(
            aws_sdk_backup_gateway.types.virtual_machine.deserialize_aws_json_1_0(item)
        )
    return out
