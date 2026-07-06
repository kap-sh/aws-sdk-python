"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateStorageVirtualMachineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.storage_virtual_machine


class UpdateStorageVirtualMachineResponse(TypedDict, closed=True):
    storage_virtual_machine: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine.StorageVirtualMachine"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStorageVirtualMachineResponse) -> dict:
    out: dict = {}
    if "storage_virtual_machine" in value:
        import aws_sdk_fsx.types.storage_virtual_machine

        out["StorageVirtualMachine"] = (
            aws_sdk_fsx.types.storage_virtual_machine.serialize_aws_json_1_1(
                value["storage_virtual_machine"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStorageVirtualMachineResponse:
    out: UpdateStorageVirtualMachineResponse = {}  # type: ignore[typeddict-item]
    if "StorageVirtualMachine" in data:
        import aws_sdk_fsx.types.storage_virtual_machine

        out["storage_virtual_machine"] = (
            aws_sdk_fsx.types.storage_virtual_machine.deserialize_aws_json_1_1(
                data["StorageVirtualMachine"]
            )
        )
    return out
