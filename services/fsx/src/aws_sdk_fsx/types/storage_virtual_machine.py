"""Generated from Smithy shape ``com.amazonaws.fsx#StorageVirtualMachine``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.creation_time
    import aws_sdk_fsx.types.file_system_id
    import aws_sdk_fsx.types.lifecycle_transition_reason
    import aws_sdk_fsx.types.resource_arn
    import aws_sdk_fsx.types.storage_virtual_machine_id
    import aws_sdk_fsx.types.storage_virtual_machine_lifecycle
    import aws_sdk_fsx.types.storage_virtual_machine_name
    import aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style
    import aws_sdk_fsx.types.storage_virtual_machine_subtype
    import aws_sdk_fsx.types.svm_active_directory_configuration
    import aws_sdk_fsx.types.svm_endpoints
    import aws_sdk_fsx.types.tags
    import aws_sdk_fsx.types.uuid


class StorageVirtualMachine(TypedDict):
    active_directory_configuration: NotRequired[
        "aws_sdk_fsx.types.svm_active_directory_configuration.SvmActiveDirectoryConfiguration"
    ]
    """<p>Describes the Microsoft Active Directory configuration to which the SVM is joined, if applicable.</p>"""
    creation_time: NotRequired["aws_sdk_fsx.types.creation_time.CreationTime"]
    endpoints: NotRequired["aws_sdk_fsx.types.svm_endpoints.SvmEndpoints"]
    """<p>The endpoints that are used to access data or to manage the SVM using the NetApp ONTAP CLI, REST API, or NetApp CloudManager. They are the <code>Iscsi</code>, <code>Management</code>, <code>Nfs</code>, and <code>Smb</code> endpoints.</p>"""
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    lifecycle: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_lifecycle.StorageVirtualMachineLifecycle"
    ]
    """<p>Describes the SVM's lifecycle status.</p> <ul> <li> <p> <code>CREATED</code> - The SVM is fully available for use.</p> </li> <li> <p> <code>CREATING</code> - Amazon FSx is creating the new SVM.</p> </li> <li> <p> <code>DELETING</code> - Amazon FSx is deleting an existing SVM.</p> </li> <li> <p> <code>FAILED</code> - Amazon FSx was unable to create the SVM.</p> </li> <li> <p> <code>MISCONFIGURED</code> - The SVM is in a failed but recoverable state.</p> </li> <li> <p> <code>PENDING</code> - Amazon FSx has not started creating the SVM.</p> </li> </ul>"""
    name: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_name.StorageVirtualMachineName"
    ]
    """<p>The name of the SVM, if provisioned.</p>"""
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]
    storage_virtual_machine_id: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_id.StorageVirtualMachineId"
    ]
    """<p>The SVM's system generated unique ID.</p>"""
    subtype: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_subtype.StorageVirtualMachineSubtype"
    ]
    """<p>Describes the SVM's subtype.</p>"""
    uuid: NotRequired["aws_sdk_fsx.types.uuid.UUID"]
    """<p>The SVM's UUID (universally unique identifier).</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]
    lifecycle_transition_reason: NotRequired[
        "aws_sdk_fsx.types.lifecycle_transition_reason.LifecycleTransitionReason"
    ]
    """<p>Describes why the SVM lifecycle state changed.</p>"""
    root_volume_security_style: NotRequired[
        "aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style.StorageVirtualMachineRootVolumeSecurityStyle"
    ]
    """<p>The security style of the root volume of the SVM.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageVirtualMachine) -> dict:
    out: dict = {}
    if "active_directory_configuration" in value:
        import aws_sdk_fsx.types.svm_active_directory_configuration

        out["ActiveDirectoryConfiguration"] = (
            aws_sdk_fsx.types.svm_active_directory_configuration.serialize_aws_json_1_1(
                value["active_directory_configuration"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_fsx.types.creation_time

        out["CreationTime"] = aws_sdk_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "endpoints" in value:
        import aws_sdk_fsx.types.svm_endpoints

        out["Endpoints"] = aws_sdk_fsx.types.svm_endpoints.serialize_aws_json_1_1(
            value["endpoints"]
        )
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.storage_virtual_machine_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.storage_virtual_machine_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "storage_virtual_machine_id" in value:
        out["StorageVirtualMachineId"] = value["storage_virtual_machine_id"]
    if "subtype" in value:
        import aws_sdk_fsx.types.storage_virtual_machine_subtype

        out["Subtype"] = (
            aws_sdk_fsx.types.storage_virtual_machine_subtype.serialize_aws_json_1_1(
                value["subtype"]
            )
        )
    if "uuid" in value:
        out["UUID"] = value["uuid"]
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "lifecycle_transition_reason" in value:
        import aws_sdk_fsx.types.lifecycle_transition_reason

        out["LifecycleTransitionReason"] = (
            aws_sdk_fsx.types.lifecycle_transition_reason.serialize_aws_json_1_1(
                value["lifecycle_transition_reason"]
            )
        )
    if "root_volume_security_style" in value:
        import aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style

        out["RootVolumeSecurityStyle"] = (
            aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style.serialize_aws_json_1_1(
                value["root_volume_security_style"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StorageVirtualMachine:
    out: StorageVirtualMachine = {}  # type: ignore[typeddict-item]
    if "ActiveDirectoryConfiguration" in data:
        import aws_sdk_fsx.types.svm_active_directory_configuration

        out["active_directory_configuration"] = (
            aws_sdk_fsx.types.svm_active_directory_configuration.deserialize_aws_json_1_1(
                data["ActiveDirectoryConfiguration"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_fsx.types.creation_time

        out["creation_time"] = aws_sdk_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "Endpoints" in data:
        import aws_sdk_fsx.types.svm_endpoints

        out["endpoints"] = aws_sdk_fsx.types.svm_endpoints.deserialize_aws_json_1_1(
            data["Endpoints"]
        )
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.storage_virtual_machine_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.storage_virtual_machine_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "StorageVirtualMachineId" in data:
        out["storage_virtual_machine_id"] = data["StorageVirtualMachineId"]
    if "Subtype" in data:
        import aws_sdk_fsx.types.storage_virtual_machine_subtype

        out["subtype"] = (
            aws_sdk_fsx.types.storage_virtual_machine_subtype.deserialize_aws_json_1_1(
                data["Subtype"]
            )
        )
    if "UUID" in data:
        out["uuid"] = data["UUID"]
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "LifecycleTransitionReason" in data:
        import aws_sdk_fsx.types.lifecycle_transition_reason

        out["lifecycle_transition_reason"] = (
            aws_sdk_fsx.types.lifecycle_transition_reason.deserialize_aws_json_1_1(
                data["LifecycleTransitionReason"]
            )
        )
    if "RootVolumeSecurityStyle" in data:
        import aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style

        out["root_volume_security_style"] = (
            aws_sdk_fsx.types.storage_virtual_machine_root_volume_security_style.deserialize_aws_json_1_1(
                data["RootVolumeSecurityStyle"]
            )
        )
    return out
