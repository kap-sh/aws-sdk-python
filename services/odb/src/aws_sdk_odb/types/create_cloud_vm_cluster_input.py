"""Generated from Smithy shape ``com.amazonaws.odb#CreateCloudVmClusterInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.cluster_name
    import aws_sdk_odb.types.data_collection_options
    import aws_sdk_odb.types.general_input_string
    import aws_sdk_odb.types.hostname
    import aws_sdk_odb.types.license_model
    import aws_sdk_odb.types.request_tag_map
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.string_list


class CreateCloudVmClusterInput(TypedDict):
    cloud_exadata_infrastructure_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the Exadata infrastructure for this VM cluster.</p>"""
    cpu_core_count: "int"
    """<p>The number of CPU cores to enable on the VM cluster.</p>"""
    display_name: "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
    """<p>A user-friendly name for the VM cluster.</p>"""
    gi_version: "str"
    """<p>A valid software version of Oracle Grid Infrastructure (GI). To get the list of valid values, use the <code>ListGiVersions</code> operation and specify the shape of the Exadata infrastructure.</p> <p>Example: <code>19.0.0.0</code> </p>"""
    hostname: "aws_sdk_odb.types.hostname.Hostname"
    """<p>The host name for the VM cluster.</p> <p>Constraints:</p> <ul> <li> <p>Can't be \"localhost\" or \"hostname\".</p> </li> <li> <p>Can't contain \"-version\".</p> </li> <li> <p>The maximum length of the combined hostname and domain is 63 characters.</p> </li> <li> <p>The hostname must be unique within the subnet.</p> </li> </ul>"""
    ssh_public_keys: "aws_sdk_odb.types.string_list.StringList"
    """<p>The public key portion of one or more key pairs used for SSH access to the VM cluster.</p>"""
    odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network for the VM cluster.</p>"""
    cluster_name: NotRequired["aws_sdk_odb.types.cluster_name.ClusterName"]
    """<p>A name for the Grid Infrastructure cluster. The name isn't case sensitive.</p>"""
    data_collection_options: NotRequired[
        "aws_sdk_odb.types.data_collection_options.DataCollectionOptions"
    ]
    """<p>The set of preferences for the various diagnostic collection options for the VM cluster.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The size of the data disk group, in terabytes (TBs), to allocate for the VM cluster.</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of local node storage, in gigabytes (GBs), to allocate for the VM cluster.</p>"""
    db_servers: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of database servers for the VM cluster.</p>"""
    tags: NotRequired["aws_sdk_odb.types.request_tag_map.RequestTagMap"]
    """<p>The list of resource tags to apply to the VM cluster.</p>"""
    is_local_backup_enabled: NotRequired["bool"]
    """<p>Specifies whether to enable database backups to local Exadata storage for the VM cluster.</p>"""
    is_sparse_diskgroup_enabled: NotRequired["bool"]
    """<p>Specifies whether to create a sparse disk group for the VM cluster.</p>"""
    license_model: NotRequired["aws_sdk_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model to apply to the VM cluster.</p> <p>Default: <code>LICENSE_INCLUDED</code> </p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory, in gigabytes (GBs), to allocate for the VM cluster.</p>"""
    system_version: NotRequired["str"]
    """<p>The version of the operating system of the image for the VM cluster.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone for the VM cluster. For a list of valid values for time zone, you can check the options in the console.</p> <p>Default: UTC</p>"""
    client_token: NotRequired[
        "aws_sdk_odb.types.general_input_string.GeneralInputString"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>"""
    scan_listener_port_tcp: NotRequired["int"]
    """<p>The port number for TCP connections to the single client access name (SCAN) listener. </p> <p>Valid values: <code>1024–8999</code> with the following exceptions: <code>2484</code>, <code>6100</code>, <code>6200</code>, <code>7060</code>, <code>7070</code>, <code>7085</code>, and <code>7879</code> </p> <p>Default: <code>1521</code> </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCloudVmClusterInput) -> dict:
    out: dict = {}
    out["cloudExadataInfrastructureId"] = value["cloud_exadata_infrastructure_id"]
    out["cpuCoreCount"] = value["cpu_core_count"]
    out["displayName"] = value["display_name"]
    out["giVersion"] = value["gi_version"]
    out["hostname"] = value["hostname"]
    import aws_sdk_odb.types.string_list

    out["sshPublicKeys"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
        value["ssh_public_keys"]
    )
    out["odbNetworkId"] = value["odb_network_id"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "data_collection_options" in value:
        import aws_sdk_odb.types.data_collection_options

        out["dataCollectionOptions"] = (
            aws_sdk_odb.types.data_collection_options.serialize_aws_json_1_0(
                value["data_collection_options"]
            )
        )
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = value["data_storage_size_in_t_bs"]
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "db_servers" in value:
        import aws_sdk_odb.types.string_list

        out["dbServers"] = aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
            value["db_servers"]
        )
    if "tags" in value:
        import aws_sdk_odb.types.request_tag_map

        out["tags"] = aws_sdk_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "is_local_backup_enabled" in value:
        out["isLocalBackupEnabled"] = value["is_local_backup_enabled"]
    if "is_sparse_diskgroup_enabled" in value:
        out["isSparseDiskgroupEnabled"] = value["is_sparse_diskgroup_enabled"]
    if "license_model" in value:
        import aws_sdk_odb.types.license_model

        out["licenseModel"] = aws_sdk_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "system_version" in value:
        out["systemVersion"] = value["system_version"]
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "scan_listener_port_tcp" in value:
        out["scanListenerPortTcp"] = value["scan_listener_port_tcp"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCloudVmClusterInput:
    out: CreateCloudVmClusterInput = {}  # type: ignore[typeddict-item]
    if "cloudExadataInfrastructureId" in data:
        out["cloud_exadata_infrastructure_id"] = data["cloudExadataInfrastructureId"]
    else:
        raise DeserializationError(
            "CreateCloudVmClusterInput.cloud_exadata_infrastructure_id required"
        )
    if "cpuCoreCount" in data:
        out["cpu_core_count"] = data["cpuCoreCount"]
    else:
        raise DeserializationError("CreateCloudVmClusterInput.cpu_core_count required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateCloudVmClusterInput.display_name required")
    if "giVersion" in data:
        out["gi_version"] = data["giVersion"]
    else:
        raise DeserializationError("CreateCloudVmClusterInput.gi_version required")
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    else:
        raise DeserializationError("CreateCloudVmClusterInput.hostname required")
    if "sshPublicKeys" in data:
        import aws_sdk_odb.types.string_list

        out["ssh_public_keys"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["sshPublicKeys"]
        )
    else:
        raise DeserializationError("CreateCloudVmClusterInput.ssh_public_keys required")
    if "odbNetworkId" in data:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        raise DeserializationError("CreateCloudVmClusterInput.odb_network_id required")
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "dataCollectionOptions" in data:
        import aws_sdk_odb.types.data_collection_options

        out["data_collection_options"] = (
            aws_sdk_odb.types.data_collection_options.deserialize_aws_json_1_0(
                data["dataCollectionOptions"]
            )
        )
    if "dataStorageSizeInTBs" in data:
        out["data_storage_size_in_t_bs"] = data["dataStorageSizeInTBs"]
    if "dbNodeStorageSizeInGBs" in data:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if "dbServers" in data:
        import aws_sdk_odb.types.string_list

        out["db_servers"] = aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
            data["dbServers"]
        )
    if "tags" in data:
        import aws_sdk_odb.types.request_tag_map

        out["tags"] = aws_sdk_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "isLocalBackupEnabled" in data:
        out["is_local_backup_enabled"] = data["isLocalBackupEnabled"]
    if "isSparseDiskgroupEnabled" in data:
        out["is_sparse_diskgroup_enabled"] = data["isSparseDiskgroupEnabled"]
    if "licenseModel" in data:
        import aws_sdk_odb.types.license_model

        out["license_model"] = aws_sdk_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if "memorySizeInGBs" in data:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if "systemVersion" in data:
        out["system_version"] = data["systemVersion"]
    if "timeZone" in data:
        out["time_zone"] = data["timeZone"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "scanListenerPortTcp" in data:
        out["scan_listener_port_tcp"] = data["scanListenerPortTcp"]
    return out
