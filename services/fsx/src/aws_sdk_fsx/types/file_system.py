"""Generated from Smithy shape ``com.amazonaws.fsx#FileSystem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.administrative_actions
    import aws_sdk_fsx.types.aws_account_id
    import aws_sdk_fsx.types.creation_time
    import aws_sdk_fsx.types.dns_name
    import aws_sdk_fsx.types.file_system_failure_details
    import aws_sdk_fsx.types.file_system_id
    import aws_sdk_fsx.types.file_system_lifecycle
    import aws_sdk_fsx.types.file_system_type
    import aws_sdk_fsx.types.file_system_type_version
    import aws_sdk_fsx.types.kms_key_id
    import aws_sdk_fsx.types.lustre_file_system_configuration
    import aws_sdk_fsx.types.network_interface_ids
    import aws_sdk_fsx.types.network_type
    import aws_sdk_fsx.types.ontap_file_system_configuration
    import aws_sdk_fsx.types.open_zfs_file_system_configuration
    import aws_sdk_fsx.types.resource_arn
    import aws_sdk_fsx.types.storage_capacity
    import aws_sdk_fsx.types.storage_type
    import aws_sdk_fsx.types.subnet_ids
    import aws_sdk_fsx.types.tags
    import aws_sdk_fsx.types.vpc_id
    import aws_sdk_fsx.types.windows_file_system_configuration


class FileSystem(TypedDict):
    owner_id: NotRequired["aws_sdk_fsx.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account that created the file system. If the file system was created by a user in IAM Identity Center, the Amazon Web Services account to which the IAM user belongs is the owner.</p>"""
    creation_time: NotRequired["aws_sdk_fsx.types.creation_time.CreationTime"]
    """<p>The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.</p>"""
    file_system_id: NotRequired["aws_sdk_fsx.types.file_system_id.FileSystemId"]
    """<p>The system-generated, unique 17-digit ID of the file system.</p>"""
    file_system_type: NotRequired["aws_sdk_fsx.types.file_system_type.FileSystemType"]
    """<p>The type of Amazon FSx file system, which can be <code>LUSTRE</code>, <code>WINDOWS</code>, <code>ONTAP</code>, or <code>OPENZFS</code>.</p>"""
    lifecycle: NotRequired[
        "aws_sdk_fsx.types.file_system_lifecycle.FileSystemLifecycle"
    ]
    """<p>The lifecycle status of the file system. The following are the possible values and what they mean:</p> <ul> <li> <p> <code>AVAILABLE</code> - The file system is in a healthy state, and is reachable and available for use.</p> </li> <li> <p> <code>CREATING</code> - Amazon FSx is creating the new file system.</p> </li> <li> <p> <code>DELETING</code> - Amazon FSx is deleting an existing file system.</p> </li> <li> <p> <code>FAILED</code> - An existing file system has experienced an unrecoverable failure. When creating a new file system, Amazon FSx was unable to create the file system.</p> </li> <li> <p> <code>MISCONFIGURED</code> - The file system is in a failed but recoverable state.</p> </li> <li> <p> <code>MISCONFIGURED_UNAVAILABLE</code> - (Amazon FSx for Windows File Server only) The file system is currently unavailable due to a change in your Active Directory configuration.</p> </li> <li> <p> <code>UPDATING</code> - The file system is undergoing a customer-initiated update.</p> </li> </ul>"""
    failure_details: NotRequired[
        "aws_sdk_fsx.types.file_system_failure_details.FileSystemFailureDetails"
    ]
    storage_capacity: NotRequired["aws_sdk_fsx.types.storage_capacity.StorageCapacity"]
    """<p>The storage capacity of the file system in gibibytes (GiB).</p> <p>Amazon FSx responds with an HTTP status code 400 (Bad Request) if the value of <code>StorageCapacity</code> is outside of the minimum or maximum values.</p>"""
    storage_type: NotRequired["aws_sdk_fsx.types.storage_type.StorageType"]
    """<p>The type of storage the file system is using.</p> <ul> <li> <p>If set to <code>SSD</code>, the file system uses solid state drive storage.</p> </li> <li> <p>If set to <code>HDD</code>, the file system uses hard disk drive storage.</p> </li> <li> <p>If set to <code>INTELLIGENT_TIERING</code>, the file system uses fully elastic, intelligently-tiered storage.</p> </li> </ul>"""
    vpc_id: NotRequired["aws_sdk_fsx.types.vpc_id.VpcId"]
    """<p>The ID of the primary virtual private cloud (VPC) for the file system.</p>"""
    subnet_ids: NotRequired["aws_sdk_fsx.types.subnet_ids.SubnetIds"]
    """<p>Specifies the IDs of the subnets that the file system is accessible from. For the Amazon FSx Windows and ONTAP <code>MULTI_AZ_1</code> file system deployment type, there are two subnet IDs, one for the preferred file server and one for the standby file server. The preferred file server subnet identified in the <code>PreferredSubnetID</code> property. All other file systems have only one subnet ID.</p> <p>For FSx for Lustre file systems, and Single-AZ Windows file systems, this is the ID of the subnet that contains the file system's endpoint. For <code>MULTI_AZ_1</code> Windows and ONTAP file systems, the file system endpoint is available in the <code>PreferredSubnetID</code>.</p>"""
    network_interface_ids: NotRequired[
        "aws_sdk_fsx.types.network_interface_ids.NetworkInterfaceIds"
    ]
    """<p>The IDs of the elastic network interfaces from which a specific file system is accessible. The elastic network interface is automatically created in the same virtual private cloud (VPC) that the Amazon FSx file system was created in. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html\">Elastic Network Interfaces</a> in the <i>Amazon EC2 User Guide.</i> </p> <p>For an Amazon FSx for Windows File Server file system, you can have one network interface ID. For an Amazon FSx for Lustre file system, you can have more than one.</p>"""
    dns_name: NotRequired["aws_sdk_fsx.types.dns_name.DNSName"]
    """<p>The Domain Name System (DNS) name for the file system.</p>"""
    kms_key_id: NotRequired["aws_sdk_fsx.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt Amazon FSx file system data. Used as follows with Amazon FSx file system types:</p> <ul> <li> <p>Amazon FSx for Lustre <code>PERSISTENT_1</code> and <code>PERSISTENT_2</code> deployment types only.</p> <p> <code>SCRATCH_1</code> and <code>SCRATCH_2</code> types are encrypted using the Amazon FSx service KMS key for your account.</p> </li> <li> <p>Amazon FSx for NetApp ONTAP</p> </li> <li> <p>Amazon FSx for OpenZFS</p> </li> <li> <p>Amazon FSx for Windows File Server</p> </li> </ul>"""
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the file system resource.</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]
    """<p>The tags to associate with the file system. For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/LustreGuide/tag-resources.html\">Tagging your Amazon FSx resources</a> in the <i>Amazon FSx for Lustre User Guide</i>.</p>"""
    windows_configuration: NotRequired[
        "aws_sdk_fsx.types.windows_file_system_configuration.WindowsFileSystemConfiguration"
    ]
    """<p>The configuration for this Amazon FSx for Windows File Server file system.</p>"""
    lustre_configuration: NotRequired[
        "aws_sdk_fsx.types.lustre_file_system_configuration.LustreFileSystemConfiguration"
    ]
    administrative_actions: NotRequired[
        "aws_sdk_fsx.types.administrative_actions.AdministrativeActions"
    ]
    """<p>A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system that you have initiated using the <code>UpdateFileSystem</code> operation.</p>"""
    ontap_configuration: NotRequired[
        "aws_sdk_fsx.types.ontap_file_system_configuration.OntapFileSystemConfiguration"
    ]
    """<p>The configuration for this Amazon FSx for NetApp ONTAP file system.</p>"""
    file_system_type_version: NotRequired[
        "aws_sdk_fsx.types.file_system_type_version.FileSystemTypeVersion"
    ]
    """<p>The Lustre version of the Amazon FSx for Lustre file system, which can be <code>2.10</code>, <code>2.12</code>, or <code>2.15</code>.</p>"""
    open_zfs_configuration: NotRequired[
        "aws_sdk_fsx.types.open_zfs_file_system_configuration.OpenZFSFileSystemConfiguration"
    ]
    """<p>The configuration for this Amazon FSx for OpenZFS file system.</p>"""
    network_type: NotRequired["aws_sdk_fsx.types.network_type.NetworkType"]
    """<p>The network type of the file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystem) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "creation_time" in value:
        import aws_sdk_fsx.types.creation_time

        out["CreationTime"] = aws_sdk_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "file_system_type" in value:
        import aws_sdk_fsx.types.file_system_type

        out["FileSystemType"] = (
            aws_sdk_fsx.types.file_system_type.serialize_aws_json_1_1(
                value["file_system_type"]
            )
        )
    if "lifecycle" in value:
        import aws_sdk_fsx.types.file_system_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.file_system_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "failure_details" in value:
        import aws_sdk_fsx.types.file_system_failure_details

        out["FailureDetails"] = (
            aws_sdk_fsx.types.file_system_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "storage_capacity" in value:
        out["StorageCapacity"] = value["storage_capacity"]
    if "storage_type" in value:
        import aws_sdk_fsx.types.storage_type

        out["StorageType"] = aws_sdk_fsx.types.storage_type.serialize_aws_json_1_1(
            value["storage_type"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_ids" in value:
        import aws_sdk_fsx.types.subnet_ids

        out["SubnetIds"] = aws_sdk_fsx.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "network_interface_ids" in value:
        import aws_sdk_fsx.types.network_interface_ids

        out["NetworkInterfaceIds"] = (
            aws_sdk_fsx.types.network_interface_ids.serialize_aws_json_1_1(
                value["network_interface_ids"]
            )
        )
    if "dns_name" in value:
        out["DNSName"] = value["dns_name"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "windows_configuration" in value:
        import aws_sdk_fsx.types.windows_file_system_configuration

        out["WindowsConfiguration"] = (
            aws_sdk_fsx.types.windows_file_system_configuration.serialize_aws_json_1_1(
                value["windows_configuration"]
            )
        )
    if "lustre_configuration" in value:
        import aws_sdk_fsx.types.lustre_file_system_configuration

        out["LustreConfiguration"] = (
            aws_sdk_fsx.types.lustre_file_system_configuration.serialize_aws_json_1_1(
                value["lustre_configuration"]
            )
        )
    if "administrative_actions" in value:
        import aws_sdk_fsx.types.administrative_actions

        out["AdministrativeActions"] = (
            aws_sdk_fsx.types.administrative_actions.serialize_aws_json_1_1(
                value["administrative_actions"]
            )
        )
    if "ontap_configuration" in value:
        import aws_sdk_fsx.types.ontap_file_system_configuration

        out["OntapConfiguration"] = (
            aws_sdk_fsx.types.ontap_file_system_configuration.serialize_aws_json_1_1(
                value["ontap_configuration"]
            )
        )
    if "file_system_type_version" in value:
        out["FileSystemTypeVersion"] = value["file_system_type_version"]
    if "open_zfs_configuration" in value:
        import aws_sdk_fsx.types.open_zfs_file_system_configuration

        out["OpenZFSConfiguration"] = (
            aws_sdk_fsx.types.open_zfs_file_system_configuration.serialize_aws_json_1_1(
                value["open_zfs_configuration"]
            )
        )
    if "network_type" in value:
        import aws_sdk_fsx.types.network_type

        out["NetworkType"] = aws_sdk_fsx.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystem:
    out: FileSystem = {}  # type: ignore[typeddict-item]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "CreationTime" in data:
        import aws_sdk_fsx.types.creation_time

        out["creation_time"] = aws_sdk_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    if "FileSystemType" in data:
        import aws_sdk_fsx.types.file_system_type

        out["file_system_type"] = (
            aws_sdk_fsx.types.file_system_type.deserialize_aws_json_1_1(
                data["FileSystemType"]
            )
        )
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.file_system_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.file_system_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "FailureDetails" in data:
        import aws_sdk_fsx.types.file_system_failure_details

        out["failure_details"] = (
            aws_sdk_fsx.types.file_system_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if "StorageCapacity" in data:
        out["storage_capacity"] = data["StorageCapacity"]
    if "StorageType" in data:
        import aws_sdk_fsx.types.storage_type

        out["storage_type"] = aws_sdk_fsx.types.storage_type.deserialize_aws_json_1_1(
            data["StorageType"]
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetIds" in data:
        import aws_sdk_fsx.types.subnet_ids

        out["subnet_ids"] = aws_sdk_fsx.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "NetworkInterfaceIds" in data:
        import aws_sdk_fsx.types.network_interface_ids

        out["network_interface_ids"] = (
            aws_sdk_fsx.types.network_interface_ids.deserialize_aws_json_1_1(
                data["NetworkInterfaceIds"]
            )
        )
    if "DNSName" in data:
        out["dns_name"] = data["DNSName"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "WindowsConfiguration" in data:
        import aws_sdk_fsx.types.windows_file_system_configuration

        out["windows_configuration"] = (
            aws_sdk_fsx.types.windows_file_system_configuration.deserialize_aws_json_1_1(
                data["WindowsConfiguration"]
            )
        )
    if "LustreConfiguration" in data:
        import aws_sdk_fsx.types.lustre_file_system_configuration

        out["lustre_configuration"] = (
            aws_sdk_fsx.types.lustre_file_system_configuration.deserialize_aws_json_1_1(
                data["LustreConfiguration"]
            )
        )
    if "AdministrativeActions" in data:
        import aws_sdk_fsx.types.administrative_actions

        out["administrative_actions"] = (
            aws_sdk_fsx.types.administrative_actions.deserialize_aws_json_1_1(
                data["AdministrativeActions"]
            )
        )
    if "OntapConfiguration" in data:
        import aws_sdk_fsx.types.ontap_file_system_configuration

        out["ontap_configuration"] = (
            aws_sdk_fsx.types.ontap_file_system_configuration.deserialize_aws_json_1_1(
                data["OntapConfiguration"]
            )
        )
    if "FileSystemTypeVersion" in data:
        out["file_system_type_version"] = data["FileSystemTypeVersion"]
    if "OpenZFSConfiguration" in data:
        import aws_sdk_fsx.types.open_zfs_file_system_configuration

        out["open_zfs_configuration"] = (
            aws_sdk_fsx.types.open_zfs_file_system_configuration.deserialize_aws_json_1_1(
                data["OpenZFSConfiguration"]
            )
        )
    if "NetworkType" in data:
        import aws_sdk_fsx.types.network_type

        out["network_type"] = aws_sdk_fsx.types.network_type.deserialize_aws_json_1_1(
            data["NetworkType"]
        )
    return out
