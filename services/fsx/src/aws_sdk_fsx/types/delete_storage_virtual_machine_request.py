"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteStorageVirtualMachineRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.storage_virtual_machine_id


class DeleteStorageVirtualMachineRequest(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    storage_virtual_machine_id: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
    ]
    """<p>The ID of the SVM that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteStorageVirtualMachineRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "storage_virtual_machine_id" in value:
        out["StorageVirtualMachineId"] = value["storage_virtual_machine_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteStorageVirtualMachineRequest:
    out: DeleteStorageVirtualMachineRequest = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "StorageVirtualMachineId" in data:
        out["storage_virtual_machine_id"] = data["StorageVirtualMachineId"]
    return out
