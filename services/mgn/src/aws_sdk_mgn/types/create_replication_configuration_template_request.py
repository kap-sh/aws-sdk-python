"""Generated from Smithy shape ``com.amazonaws.mgn#CreateReplicationConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.arn
    import aws_sdk_mgn.types.bandwidth_throttling
    import aws_sdk_mgn.types.ec2_instance_type
    import aws_sdk_mgn.types.internet_protocol
    import aws_sdk_mgn.types.replication_configuration_data_plane_routing
    import aws_sdk_mgn.types.replication_configuration_default_large_staging_disk_type
    import aws_sdk_mgn.types.replication_configuration_ebs_encryption
    import aws_sdk_mgn.types.replication_servers_security_groups_i_ds
    import aws_sdk_mgn.types.subnet_id
    import aws_sdk_mgn.types.tags_map


class CreateReplicationConfigurationTemplateRequest(TypedDict):
    staging_area_subnet_id: "aws_sdk_mgn.types.subnet_id.SubnetID"
    """<p>Request to configure the Staging Area subnet ID during Replication Settings template creation.</p>"""
    associate_default_security_group: "bool"
    """<p>Request to associate the default Application Migration Service Security group with the Replication Settings template.</p>"""
    replication_servers_security_groups_i_ds: "aws_sdk_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
    """<p>Request to configure the Replication Server Security group ID during Replication Settings template creation.</p>"""
    replication_server_instance_type: (
        "aws_sdk_mgn.types.ec2_instance_type.EC2InstanceType"
    )
    """<p>Request to configure the Replication Server instance type during Replication Settings template creation.</p>"""
    use_dedicated_replication_server: "bool"
    """<p>Request to use Dedicated Replication Servers during Replication Settings template creation.</p>"""
    default_large_staging_disk_type: "aws_sdk_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
    """<p>Request to configure the default large staging disk EBS volume type during Replication Settings template creation.</p>"""
    ebs_encryption: "aws_sdk_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
    """<p>Request to configure EBS encryption during Replication Settings template creation.</p>"""
    ebs_encryption_key_arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>Request to configure an EBS encryption key during Replication Settings template creation.</p>"""
    bandwidth_throttling: "aws_sdk_mgn.types.bandwidth_throttling.BandwidthThrottling"
    """<p>Request to configure bandwidth throttling during Replication Settings template creation.</p>"""
    data_plane_routing: "aws_sdk_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
    """<p>Request to configure data plane routing during Replication Settings template creation.</p>"""
    create_public_ip: "bool"
    """<p>Request to create Public IP during Replication Settings template creation.</p>"""
    staging_area_tags: "aws_sdk_mgn.types.tags_map.TagsMap"
    """<p>Request to configure Staging Area tags during Replication Settings template creation.</p>"""
    use_fips_endpoint: NotRequired["bool"]
    """<p>Request to use Fips Endpoint during Replication Settings template creation.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Request to configure tags during Replication Settings template creation.</p>"""
    internet_protocol: NotRequired[
        "aws_sdk_mgn.types.internet_protocol.InternetProtocol"
    ]
    """<p>Request to configure the internet protocol to IPv4 or IPv6.</p>"""
    store_snapshot_on_local_zone: NotRequired["bool"]
    """<p>Request to store snapshot on local zone during Replication Settings template creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReplicationConfigurationTemplateRequest) -> dict:
    out: dict = {}
    out["stagingAreaSubnetId"] = value["staging_area_subnet_id"]
    out["associateDefaultSecurityGroup"] = value["associate_default_security_group"]
    import aws_sdk_mgn.types.replication_servers_security_groups_i_ds

    out["replicationServersSecurityGroupsIDs"] = (
        aws_sdk_mgn.types.replication_servers_security_groups_i_ds.serialize_json(
            value["replication_servers_security_groups_i_ds"]
        )
    )
    out["replicationServerInstanceType"] = value["replication_server_instance_type"]
    out["useDedicatedReplicationServer"] = value["use_dedicated_replication_server"]
    out["defaultLargeStagingDiskType"] = value["default_large_staging_disk_type"]
    out["ebsEncryption"] = value["ebs_encryption"]
    if "ebs_encryption_key_arn" in value:
        out["ebsEncryptionKeyArn"] = value["ebs_encryption_key_arn"]
    out["bandwidthThrottling"] = value.get("bandwidth_throttling", 0)
    out["dataPlaneRouting"] = value["data_plane_routing"]
    out["createPublicIP"] = value["create_public_ip"]
    import aws_sdk_mgn.types.tags_map

    out["stagingAreaTags"] = aws_sdk_mgn.types.tags_map.serialize_json(
        value["staging_area_tags"]
    )
    if "use_fips_endpoint" in value:
        out["useFipsEndpoint"] = value["use_fips_endpoint"]
    if "tags" in value:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.serialize_json(value["tags"])
    if "internet_protocol" in value:
        out["internetProtocol"] = value["internet_protocol"]
    if "store_snapshot_on_local_zone" in value:
        out["storeSnapshotOnLocalZone"] = value["store_snapshot_on_local_zone"]
    return out


def deserialize_json(data: dict) -> CreateReplicationConfigurationTemplateRequest:
    out: CreateReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
    if "stagingAreaSubnetId" in data:
        out["staging_area_subnet_id"] = data["stagingAreaSubnetId"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.staging_area_subnet_id required"
        )
    if "associateDefaultSecurityGroup" in data:
        out["associate_default_security_group"] = data["associateDefaultSecurityGroup"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.associate_default_security_group required"
        )
    if "replicationServersSecurityGroupsIDs" in data:
        import aws_sdk_mgn.types.replication_servers_security_groups_i_ds

        out["replication_servers_security_groups_i_ds"] = (
            aws_sdk_mgn.types.replication_servers_security_groups_i_ds.deserialize_json(
                data["replicationServersSecurityGroupsIDs"]
            )
        )
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.replication_servers_security_groups_i_ds required"
        )
    if "replicationServerInstanceType" in data:
        out["replication_server_instance_type"] = data["replicationServerInstanceType"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.replication_server_instance_type required"
        )
    if "useDedicatedReplicationServer" in data:
        out["use_dedicated_replication_server"] = data["useDedicatedReplicationServer"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.use_dedicated_replication_server required"
        )
    if "defaultLargeStagingDiskType" in data:
        out["default_large_staging_disk_type"] = data["defaultLargeStagingDiskType"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.default_large_staging_disk_type required"
        )
    if "ebsEncryption" in data:
        out["ebs_encryption"] = data["ebsEncryption"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.ebs_encryption required"
        )
    if "ebsEncryptionKeyArn" in data:
        out["ebs_encryption_key_arn"] = data["ebsEncryptionKeyArn"]
    if "bandwidthThrottling" in data:
        out["bandwidth_throttling"] = data["bandwidthThrottling"]
    else:
        out["bandwidth_throttling"] = 0
    if "dataPlaneRouting" in data:
        out["data_plane_routing"] = data["dataPlaneRouting"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.data_plane_routing required"
        )
    if "createPublicIP" in data:
        out["create_public_ip"] = data["createPublicIP"]
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.create_public_ip required"
        )
    if "stagingAreaTags" in data:
        import aws_sdk_mgn.types.tags_map

        out["staging_area_tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(
            data["stagingAreaTags"]
        )
    else:
        raise DeserializationError(
            "CreateReplicationConfigurationTemplateRequest.staging_area_tags required"
        )
    if "useFipsEndpoint" in data:
        out["use_fips_endpoint"] = data["useFipsEndpoint"]
    if "tags" in data:
        import aws_sdk_mgn.types.tags_map

        out["tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(data["tags"])
    if "internetProtocol" in data:
        out["internet_protocol"] = data["internetProtocol"]
    if "storeSnapshotOnLocalZone" in data:
        out["store_snapshot_on_local_zone"] = data["storeSnapshotOnLocalZone"]
    return out
