"""Generated from Smithy shape ``com.amazonaws.fsx#CreateStorageVirtualMachineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.storage_virtual_machine


class CreateStorageVirtualMachineResponse(TypedDict, closed=True):
    storage_virtual_machine: NotRequired[
        "capo_fsx.types.storage_virtual_machine.StorageVirtualMachine"
    ]
    """<p>Returned after a successful <code>CreateStorageVirtualMachine</code> operation; describes the SVM just created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStorageVirtualMachineResponse) -> dict:
    out: dict = {}
    if "storage_virtual_machine" in value:
        import capo_fsx.types.storage_virtual_machine

        out["StorageVirtualMachine"] = (
            capo_fsx.types.storage_virtual_machine.serialize_aws_json_1_1(
                value["storage_virtual_machine"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStorageVirtualMachineResponse:
    out: CreateStorageVirtualMachineResponse = {}  # type: ignore[typeddict-item]
    if "StorageVirtualMachine" in data:
        import capo_fsx.types.storage_virtual_machine

        out["storage_virtual_machine"] = (
            capo_fsx.types.storage_virtual_machine.deserialize_aws_json_1_1(
                data["StorageVirtualMachine"]
            )
        )
    return out
