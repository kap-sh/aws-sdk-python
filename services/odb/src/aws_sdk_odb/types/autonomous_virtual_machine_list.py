"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousVirtualMachineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_virtual_machine_summary

AutonomousVirtualMachineList: TypeAlias = list[
    "aws_sdk_odb.types.autonomous_virtual_machine_summary.AutonomousVirtualMachineSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousVirtualMachineList) -> list:
    import aws_sdk_odb.types.autonomous_virtual_machine_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_odb.types.autonomous_virtual_machine_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutonomousVirtualMachineList:
    import aws_sdk_odb.types.autonomous_virtual_machine_summary

    out: AutonomousVirtualMachineList = []
    for item in data:
        out.append(
            aws_sdk_odb.types.autonomous_virtual_machine_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
