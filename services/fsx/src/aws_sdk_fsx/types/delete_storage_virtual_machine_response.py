"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteStorageVirtualMachineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.storage_virtual_machine_id
    import aws_sdk_fsx.types.storage_virtual_machine_lifecycle


class DeleteStorageVirtualMachineResponse(TypedDict, closed=True):
    storage_virtual_machine_id: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
    ]
    """<p>The ID of the SVM Amazon FSx is deleting.</p>"""
    lifecycle: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_lifecycle.StorageVirtualMachineLifecycle"
    ]
    """<p>Describes the lifecycle state of the SVM being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStorageVirtualMachineResponse) -> dict:
    out: dict = {}
    if "storage_virtual_machine_id" in value:
        out["StorageVirtualMachineId"] = value["storage_virtual_machine_id"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.storage_virtual_machine_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.storage_virtual_machine_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStorageVirtualMachineResponse:
    out: DeleteStorageVirtualMachineResponse = {}  # type: ignore[typeddict-item]
    if "StorageVirtualMachineId" in data:
        out["storage_virtual_machine_id"] = data["StorageVirtualMachineId"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.storage_virtual_machine_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.storage_virtual_machine_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    return out
