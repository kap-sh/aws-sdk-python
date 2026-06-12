"""Generated from Smithy shape ``com.amazonaws.backupgateway#VirtualMachineDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.name
    import aws_sdk_backup_gateway.types.path
    import aws_sdk_backup_gateway.types.resource_arn
    import aws_sdk_backup_gateway.types.string
    import aws_sdk_backup_gateway.types.time
    import aws_sdk_backup_gateway.types.vmware_tags


class VirtualMachineDetails(TypedDict):
    host_name: NotRequired["aws_sdk_backup_gateway.types.name.Name"]
    """<p>The host name of the virtual machine.</p>"""
    hypervisor_id: NotRequired["aws_sdk_backup_gateway.types.string.string"]
    """<p>The ID of the virtual machine's hypervisor.</p>"""
    name: NotRequired["aws_sdk_backup_gateway.types.name.Name"]
    """<p>The name of the virtual machine.</p>"""
    path: NotRequired["aws_sdk_backup_gateway.types.path.Path"]
    """<p>The path of the virtual machine.</p>"""
    resource_arn: NotRequired["aws_sdk_backup_gateway.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the virtual machine. For example, <code>arn:aws:backup-gateway:us-west-1:0000000000000:vm/vm-0000ABCDEFGIJKL</code>.</p>"""
    last_backup_date: NotRequired["aws_sdk_backup_gateway.types.time.Time"]
    """<p>The most recent date a virtual machine was backed up, in Unix format and UTC time.</p>"""
    vmware_tags: NotRequired["aws_sdk_backup_gateway.types.vmware_tags.VmwareTags"]
    """<p>These are the details of the VMware tags associated with the specified virtual machine.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VirtualMachineDetails) -> dict:
    out: dict = {}
    if "host_name" in value:
        out["HostName"] = value["host_name"]
    if "hypervisor_id" in value:
        out["HypervisorId"] = value["hypervisor_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "path" in value:
        out["Path"] = value["path"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "last_backup_date" in value:
        import aws_sdk_backup_gateway.types.time

        out["LastBackupDate"] = (
            aws_sdk_backup_gateway.types.time.serialize_aws_json_1_0(
                value["last_backup_date"]
            )
        )
    if "vmware_tags" in value:
        import aws_sdk_backup_gateway.types.vmware_tags

        out["VmwareTags"] = (
            aws_sdk_backup_gateway.types.vmware_tags.serialize_aws_json_1_0(
                value["vmware_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VirtualMachineDetails:
    out: VirtualMachineDetails = {}  # type: ignore[typeddict-item]
    if "HostName" in data:
        out["host_name"] = data["HostName"]
    if "HypervisorId" in data:
        out["hypervisor_id"] = data["HypervisorId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Path" in data:
        out["path"] = data["Path"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "LastBackupDate" in data:
        import aws_sdk_backup_gateway.types.time

        out["last_backup_date"] = (
            aws_sdk_backup_gateway.types.time.deserialize_aws_json_1_0(
                data["LastBackupDate"]
            )
        )
    if "VmwareTags" in data:
        import aws_sdk_backup_gateway.types.vmware_tags

        out["vmware_tags"] = (
            aws_sdk_backup_gateway.types.vmware_tags.deserialize_aws_json_1_0(
                data["VmwareTags"]
            )
        )
    return out
