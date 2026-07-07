"""Generated from Smithy shape ``com.amazonaws.fsx#CreateStorageVirtualMachineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.admin_password
    import aws_sdk_fsx.types.client_request_token
    import aws_sdk_fsx.types.create_svm_active_directory_configuration
    import aws_sdk_fsx.types.file_system_id
    import aws_sdk_fsx.types.storage_virtual_machine_name
    import aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style
    import aws_sdk_fsx.types.tags


class CreateStorageVirtualMachineRequest(TypedDict, closed=True):
    active_directory_configuration: NotRequired[
        "aws_sdk_fsx.types.create_svm_active_directory_configuration.CreateSvmActiveDirectoryConfiguration"
    ]
    """<p>Describes the self-managed Microsoft Active Directory to which you want to join the SVM. Joining an Active Directory provides user authentication and access control for SMB clients, including Microsoft Windows and macOS clients accessing the file system.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_fsx.types.client_request_token.ClientRequestToken"
    ]
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    name: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_name.StorageVirtualMachineName"
    ]
    """<p>The name of the SVM.</p>"""
    svm_admin_password: NotRequired["aws_sdk_fsx.types.admin_password.AdminPassword"]
    """<p>The password to use when managing the SVM using the NetApp ONTAP CLI or REST API. If you do not specify a password, you can still use the file system's <code>fsxadmin</code> user to manage the SVM.</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]
    root_volume_security_style: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style.StorageVirtualMachineRootVolumeSecurityStyle"
    ]
    r"""<p>The security style of the root volume of the SVM. Specify one of the following values:</p> <ul> <li> <p> <code>UNIX</code> if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account.</p> </li> <li> <p> <code>NTFS</code> if the file system is managed by a Microsoft Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Microsoft Windows user as the service account.</p> </li> <li> <p> <code>MIXED</code> This is an advanced setting. For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-security-style.html\">Volume security style</a> in the Amazon FSx for NetApp ONTAP User Guide.</p> </li> </ul> <p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStorageVirtualMachineRequest) -> dict:
    out: dict = {}
    if "active_directory_configuration" in value:
        import aws_sdk_fsx.types.create_svm_active_directory_configuration

        out["ActiveDirectoryConfiguration"] = (
            aws_sdk_fsx.types.create_svm_active_directory_configuration.serialize_aws_json_1_1(
                value["active_directory_configuration"]
            )
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "svm_admin_password" in value:
        out["SvmAdminPassword"] = value["svm_admin_password"]
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "root_volume_security_style" in value:
        import aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style

        out["RootVolumeSecurityStyle"] = (
            aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style.serialize_aws_json_1_1(
                value["root_volume_security_style"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStorageVirtualMachineRequest:
    out: CreateStorageVirtualMachineRequest = {}  # type: ignore[typeddict-item]
    if "ActiveDirectoryConfiguration" in data:
        import aws_sdk_fsx.types.create_svm_active_directory_configuration

        out["active_directory_configuration"] = (
            aws_sdk_fsx.types.create_svm_active_directory_configuration.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfiguration"]
            )
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SvmAdminPassword" in data:
        out["svm_admin_password"] = data["SvmAdminPassword"]
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "RootVolumeSecurityStyle" in data:
        import aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style

        out["root_volume_security_style"] = (
            aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style.deserialize_aws_json_1_1(
                data["RootVolumeSecurityStyle"]
            )
        )
    return out
