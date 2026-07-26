"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateStorageVirtualMachineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.admin_password
    import capo_fsx.types.client_request_token
    import capo_fsx.types.storage_virtual_machine_id
    import capo_fsx.types.update_svm_active_directory_configuration


class UpdateStorageVirtualMachineRequest(TypedDict, closed=True):
    active_directory_configuration: NotRequired[
        "capo_fsx.types.update_svm_active_directory_configuration.UpdateSvmActiveDirectoryConfiguration"
    ]
    """<p>Specifies updates to an SVM's Microsoft Active Directory (AD) configuration.</p>"""
    client_request_token: NotRequired[
        "capo_fsx.types.client_request_token.ClientRequestToken"
    ]
    storage_virtual_machine_id: NotRequired[
        "capo_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
    ]
    """<p>The ID of the SVM that you want to update, in the format <code>svm-0123456789abcdef0</code>.</p>"""
    svm_admin_password: NotRequired["capo_fsx.types.admin_password.AdminPassword"]
    """<p>Specifies a new SvmAdminPassword.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStorageVirtualMachineRequest) -> dict:
    out: dict = {}
    if "active_directory_configuration" in value:
        import capo_fsx.types.update_svm_active_directory_configuration

        out["ActiveDirectoryConfiguration"] = (
            capo_fsx.types.update_svm_active_directory_configuration.serialize_aws_json_1_1(
                value["active_directory_configuration"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "storage_virtual_machine_id" in value:
        out["StorageVirtualMachineId"] = value["storage_virtual_machine_id"]
    if "svm_admin_password" in value:
        out["SvmAdminPassword"] = value["svm_admin_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStorageVirtualMachineRequest:
    out: UpdateStorageVirtualMachineRequest = {}  # type: ignore[typeddict-item]
    if "ActiveDirectoryConfiguration" in data:
        import capo_fsx.types.update_svm_active_directory_configuration

        out["active_directory_configuration"] = (
            capo_fsx.types.update_svm_active_directory_configuration.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfiguration"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "StorageVirtualMachineId" in data:
        out["storage_virtual_machine_id"] = data["StorageVirtualMachineId"]
    if "SvmAdminPassword" in data:
        out["svm_admin_password"] = data["SvmAdminPassword"]
    return out
