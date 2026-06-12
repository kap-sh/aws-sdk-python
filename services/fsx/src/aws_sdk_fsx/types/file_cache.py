"""Generated from Smithy shape ``com.amazonaws.fsx#FileCache``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.aws_account_id
    import aws_sdk_fsx.types.creation_time
    import aws_sdk_fsx.types.data_repository_association_ids
    import aws_sdk_fsx.types.dns_name
    import aws_sdk_fsx.types.file_cache_failure_details
    import aws_sdk_fsx.types.file_cache_id
    import aws_sdk_fsx.types.file_cache_lifecycle
    import aws_sdk_fsx.types.file_cache_lustre_configuration
    import aws_sdk_fsx.types.file_cache_type
    import aws_sdk_fsx.types.file_system_type_version
    import aws_sdk_fsx.types.kms_key_id
    import aws_sdk_fsx.types.network_interface_ids
    import aws_sdk_fsx.types.resource_arn
    import aws_sdk_fsx.types.storage_capacity
    import aws_sdk_fsx.types.subnet_ids
    import aws_sdk_fsx.types.vpc_id


class FileCache(TypedDict):
    owner_id: NotRequired["aws_sdk_fsx.types.aws_account_id.AWSAccountId"]
    creation_time: NotRequired["aws_sdk_fsx.types.creation_time.CreationTime"]
    file_cache_id: NotRequired["aws_sdk_fsx.types.file_cache_id.FileCacheId"]
    """<p>The system-generated, unique ID of the cache.</p>"""
    file_cache_type: NotRequired["aws_sdk_fsx.types.file_cache_type.FileCacheType"]
    """<p>The type of cache, which must be <code>LUSTRE</code>.</p>"""
    file_cache_type_version: NotRequired[
        "aws_sdk_fsx.types.file_system_type_version.FileSystemTypeVersion"
    ]
    """<p>The Lustre version of the cache, which must be <code>2.12</code>.</p>"""
    lifecycle: NotRequired["aws_sdk_fsx.types.file_cache_lifecycle.FileCacheLifecycle"]
    """<p>The lifecycle status of the cache. The following are the possible values and what they mean:</p> <ul> <li> <p> <code>AVAILABLE</code> - The cache is in a healthy state, and is reachable and available for use.</p> </li> <li> <p> <code>CREATING</code> - The new cache is being created.</p> </li> <li> <p> <code>DELETING</code> - An existing cache is being deleted.</p> </li> <li> <p> <code>UPDATING</code> - The cache is undergoing a customer-initiated update.</p> </li> <li> <p> <code>FAILED</code> - An existing cache has experienced an unrecoverable failure. When creating a new cache, the cache was unable to be created.</p> </li> </ul>"""
    failure_details: NotRequired[
        "aws_sdk_fsx.types.file_cache_failure_details.FileCacheFailureDetails"
    ]
    """<p>A structure providing details of any failures that occurred.</p>"""
    storage_capacity: NotRequired["aws_sdk_fsx.types.storage_capacity.StorageCapacity"]
    """<p>The storage capacity of the cache in gibibytes (GiB).</p>"""
    vpc_id: NotRequired["aws_sdk_fsx.types.vpc_id.VpcId"]
    subnet_ids: NotRequired["aws_sdk_fsx.types.subnet_ids.SubnetIds"]
    network_interface_ids: NotRequired[
        "aws_sdk_fsx.types.network_interface_ids.NetworkInterfaceIds"
    ]
    dns_name: NotRequired["aws_sdk_fsx.types.dns_name.DNSName"]
    """<p>The Domain Name System (DNS) name for the cache.</p>"""
    kms_key_id: NotRequired["aws_sdk_fsx.types.kms_key_id.KmsKeyId"]
    """<p>Specifies the ID of the Key Management Service (KMS) key to use for encrypting data on an Amazon File Cache. If a <code>KmsKeyId</code> isn't specified, the Amazon FSx-managed KMS key for your account is used. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html\">Encrypt</a> in the <i>Key Management Service API Reference</i>.</p>"""
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]
    lustre_configuration: NotRequired[
        "aws_sdk_fsx.types.file_cache_lustre_configuration.FileCacheLustreConfiguration"
    ]
    """<p>The configuration for the Amazon File Cache resource.</p>"""
    data_repository_association_ids: NotRequired[
        "aws_sdk_fsx.types.data_repository_association_ids.DataRepositoryAssociationIds"
    ]
    """<p>A list of IDs of data repository associations that are associated with this cache.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileCache) -> dict:
    out: dict = {}
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "creation_time" in value:
        import aws_sdk_fsx.types.creation_time

        out["CreationTime"] = aws_sdk_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "file_cache_id" in value:
        out["FileCacheId"] = value["file_cache_id"]
    if "file_cache_type" in value:
        import aws_sdk_fsx.types.file_cache_type

        out["FileCacheType"] = aws_sdk_fsx.types.file_cache_type.serialize_aws_json_1_1(
            value["file_cache_type"]
        )
    if "file_cache_type_version" in value:
        out["FileCacheTypeVersion"] = value["file_cache_type_version"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.file_cache_lifecycle

        out["Lifecycle"] = (
            aws_sdk_fsx.types.file_cache_lifecycle.serialize_aws_json_1_1(
                value["lifecycle"]
            )
        )
    if "failure_details" in value:
        import aws_sdk_fsx.types.file_cache_failure_details

        out["FailureDetails"] = (
            aws_sdk_fsx.types.file_cache_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "storage_capacity" in value:
        out["StorageCapacity"] = value["storage_capacity"]
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
    if "lustre_configuration" in value:
        import aws_sdk_fsx.types.file_cache_lustre_configuration

        out["LustreConfiguration"] = (
            aws_sdk_fsx.types.file_cache_lustre_configuration.serialize_aws_json_1_1(
                value["lustre_configuration"]
            )
        )
    if "data_repository_association_ids" in value:
        import aws_sdk_fsx.types.data_repository_association_ids

        out["DataRepositoryAssociationIds"] = (
            aws_sdk_fsx.types.data_repository_association_ids.serialize_aws_json_1_1(
                value["data_repository_association_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileCache:
    out: FileCache = {}  # type: ignore[typeddict-item]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "CreationTime" in data:
        import aws_sdk_fsx.types.creation_time

        out["creation_time"] = aws_sdk_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "FileCacheId" in data:
        out["file_cache_id"] = data["FileCacheId"]
    if "FileCacheType" in data:
        import aws_sdk_fsx.types.file_cache_type

        out["file_cache_type"] = (
            aws_sdk_fsx.types.file_cache_type.deserialize_aws_json_1_1(
                data["FileCacheType"]
            )
        )
    if "FileCacheTypeVersion" in data:
        out["file_cache_type_version"] = data["FileCacheTypeVersion"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.file_cache_lifecycle

        out["lifecycle"] = (
            aws_sdk_fsx.types.file_cache_lifecycle.deserialize_aws_json_1_1(
                data["Lifecycle"]
            )
        )
    if "FailureDetails" in data:
        import aws_sdk_fsx.types.file_cache_failure_details

        out["failure_details"] = (
            aws_sdk_fsx.types.file_cache_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if "StorageCapacity" in data:
        out["storage_capacity"] = data["StorageCapacity"]
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
    if "LustreConfiguration" in data:
        import aws_sdk_fsx.types.file_cache_lustre_configuration

        out["lustre_configuration"] = (
            aws_sdk_fsx.types.file_cache_lustre_configuration.deserialize_aws_json_1_1(
                data["LustreConfiguration"]
            )
        )
    if "DataRepositoryAssociationIds" in data:
        import aws_sdk_fsx.types.data_repository_association_ids

        out["data_repository_association_ids"] = (
            aws_sdk_fsx.types.data_repository_association_ids.deserialize_aws_json_1_1(
                data["DataRepositoryAssociationIds"]
            )
        )
    return out
