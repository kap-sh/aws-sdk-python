"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateReplicationConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.bandwidth_throttling
    import capo_mgn.types.ec2_instance_type
    import capo_mgn.types.internet_protocol
    import capo_mgn.types.replication_configuration_data_plane_routing
    import capo_mgn.types.replication_configuration_default_large_staging_disk_type
    import capo_mgn.types.replication_configuration_ebs_encryption
    import capo_mgn.types.replication_configuration_template_id
    import capo_mgn.types.replication_servers_security_groups_i_ds
    import capo_mgn.types.subnet_id
    import capo_mgn.types.tags_map


class UpdateReplicationConfigurationTemplateRequest(TypedDict, closed=True):
    replication_configuration_template_id: "capo_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID"
    """<p>Update replication configuration template template ID request.</p>"""
    arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>Update replication configuration template ARN request.</p>"""
    staging_area_subnet_id: NotRequired["capo_mgn.types.subnet_id.SubnetID"]
    """<p>Update replication configuration template Staging Area subnet ID request.</p>"""
    associate_default_security_group: NotRequired["bool"]
    """<p>Update replication configuration template associate default Application Migration Service Security group request.</p>"""
    replication_servers_security_groups_i_ds: NotRequired[
        "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
    ]
    """<p>Update replication configuration template Replication Server Security groups IDs request.</p>"""
    replication_server_instance_type: NotRequired[
        "capo_mgn.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>Update replication configuration template Replication Server instance type request.</p>"""
    use_dedicated_replication_server: NotRequired["bool"]
    """<p>Update replication configuration template use dedicated Replication Server request.</p>"""
    default_large_staging_disk_type: NotRequired[
        "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
    ]
    """<p>Update replication configuration template use default large Staging Disk type request.</p>"""
    ebs_encryption: NotRequired[
        "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
    ]
    """<p>Update replication configuration template EBS encryption request.</p>"""
    ebs_encryption_key_arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>Update replication configuration template EBS encryption key ARN request.</p>"""
    bandwidth_throttling: "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
    """<p>Update replication configuration template bandwidth throttling request.</p>"""
    data_plane_routing: NotRequired[
        "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
    ]
    """<p>Update replication configuration template data plane routing request.</p>"""
    create_public_ip: NotRequired["bool"]
    """<p>Update replication configuration template create Public IP request.</p>"""
    staging_area_tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Update replication configuration template Staging Area Tags request.</p>"""
    use_fips_endpoint: NotRequired["bool"]
    """<p>Update replication configuration template use Fips Endpoint request.</p>"""
    internet_protocol: NotRequired["capo_mgn.types.internet_protocol.InternetProtocol"]
    """<p>Update replication configuration template internet protocol request.</p>"""
    store_snapshot_on_local_zone: NotRequired["bool"]
    """<p>Update replication configuration template store snapshot on local zone request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReplicationConfigurationTemplateRequest) -> dict:
    out: dict = {}
    out["replicationConfigurationTemplateID"] = value[
        "replication_configuration_template_id"
    ]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "staging_area_subnet_id" in value:
        out["stagingAreaSubnetId"] = value["staging_area_subnet_id"]
    if "associate_default_security_group" in value:
        out["associateDefaultSecurityGroup"] = value["associate_default_security_group"]
    if "replication_servers_security_groups_i_ds" in value:
        import capo_mgn.types.replication_servers_security_groups_i_ds

        out["replicationServersSecurityGroupsIDs"] = (
            capo_mgn.types.replication_servers_security_groups_i_ds.serialize_json(
                value["replication_servers_security_groups_i_ds"]
            )
        )
    if "replication_server_instance_type" in value:
        out["replicationServerInstanceType"] = value["replication_server_instance_type"]
    if "use_dedicated_replication_server" in value:
        out["useDedicatedReplicationServer"] = value["use_dedicated_replication_server"]
    if "default_large_staging_disk_type" in value:
        out["defaultLargeStagingDiskType"] = value["default_large_staging_disk_type"]
    if "ebs_encryption" in value:
        out["ebsEncryption"] = value["ebs_encryption"]
    if "ebs_encryption_key_arn" in value:
        out["ebsEncryptionKeyArn"] = value["ebs_encryption_key_arn"]
    out["bandwidthThrottling"] = value.get("bandwidth_throttling", 0)
    if "data_plane_routing" in value:
        out["dataPlaneRouting"] = value["data_plane_routing"]
    if "create_public_ip" in value:
        out["createPublicIP"] = value["create_public_ip"]
    if "staging_area_tags" in value:
        import capo_mgn.types.tags_map

        out["stagingAreaTags"] = capo_mgn.types.tags_map.serialize_json(
            value["staging_area_tags"]
        )
    if "use_fips_endpoint" in value:
        out["useFipsEndpoint"] = value["use_fips_endpoint"]
    if "internet_protocol" in value:
        out["internetProtocol"] = value["internet_protocol"]
    if "store_snapshot_on_local_zone" in value:
        out["storeSnapshotOnLocalZone"] = value["store_snapshot_on_local_zone"]
    return out


def deserialize_json(data: dict) -> UpdateReplicationConfigurationTemplateRequest:
    out: UpdateReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
    if "replicationConfigurationTemplateID" in data:
        out["replication_configuration_template_id"] = data[
            "replicationConfigurationTemplateID"
        ]
    else:
        raise DeserializationError(
            "UpdateReplicationConfigurationTemplateRequest.replication_configuration_template_id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "stagingAreaSubnetId" in data:
        out["staging_area_subnet_id"] = data["stagingAreaSubnetId"]
    if "associateDefaultSecurityGroup" in data:
        out["associate_default_security_group"] = data["associateDefaultSecurityGroup"]
    if "replicationServersSecurityGroupsIDs" in data:
        import capo_mgn.types.replication_servers_security_groups_i_ds

        out["replication_servers_security_groups_i_ds"] = (
            capo_mgn.types.replication_servers_security_groups_i_ds.deserialize_json(
                data["replicationServersSecurityGroupsIDs"]
            )
        )
    if "replicationServerInstanceType" in data:
        out["replication_server_instance_type"] = data["replicationServerInstanceType"]
    if "useDedicatedReplicationServer" in data:
        out["use_dedicated_replication_server"] = data["useDedicatedReplicationServer"]
    if "defaultLargeStagingDiskType" in data:
        out["default_large_staging_disk_type"] = data["defaultLargeStagingDiskType"]
    if "ebsEncryption" in data:
        out["ebs_encryption"] = data["ebsEncryption"]
    if "ebsEncryptionKeyArn" in data:
        out["ebs_encryption_key_arn"] = data["ebsEncryptionKeyArn"]
    if "bandwidthThrottling" in data:
        out["bandwidth_throttling"] = data["bandwidthThrottling"]
    else:
        out["bandwidth_throttling"] = 0
    if "dataPlaneRouting" in data:
        out["data_plane_routing"] = data["dataPlaneRouting"]
    if "createPublicIP" in data:
        out["create_public_ip"] = data["createPublicIP"]
    if "stagingAreaTags" in data:
        import capo_mgn.types.tags_map

        out["staging_area_tags"] = capo_mgn.types.tags_map.deserialize_json(
            data["stagingAreaTags"]
        )
    if "useFipsEndpoint" in data:
        out["use_fips_endpoint"] = data["useFipsEndpoint"]
    if "internetProtocol" in data:
        out["internet_protocol"] = data["internetProtocol"]
    if "storeSnapshotOnLocalZone" in data:
        out["store_snapshot_on_local_zone"] = data["storeSnapshotOnLocalZone"]
    return out
