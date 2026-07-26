"""Generated from Smithy shape ``com.amazonaws.mgn#ReplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.bandwidth_throttling
    import capo_mgn.types.ec2_instance_type
    import capo_mgn.types.internet_protocol
    import capo_mgn.types.replication_configuration_data_plane_routing
    import capo_mgn.types.replication_configuration_default_large_staging_disk_type
    import capo_mgn.types.replication_configuration_ebs_encryption
    import capo_mgn.types.replication_configuration_replicated_disks
    import capo_mgn.types.replication_servers_security_groups_i_ds
    import capo_mgn.types.small_bounded_string
    import capo_mgn.types.source_server_id
    import capo_mgn.types.subnet_id
    import capo_mgn.types.tags_map


class ReplicationConfiguration(TypedDict, closed=True):
    source_server_id: NotRequired["capo_mgn.types.source_server_id.SourceServerID"]
    """<p>Replication Configuration Source Server ID.</p>"""
    name: NotRequired["capo_mgn.types.small_bounded_string.SmallBoundedString"]
    """<p>Replication Configuration name.</p>"""
    staging_area_subnet_id: NotRequired["capo_mgn.types.subnet_id.SubnetID"]
    """<p>Replication Configuration Staging Area subnet ID.</p>"""
    associate_default_security_group: NotRequired["bool"]
    """<p>Replication Configuration associate default Application Migration Service Security Group.</p>"""
    replication_servers_security_groups_i_ds: NotRequired[
        "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
    ]
    """<p>Replication Configuration Replication Server Security Group IDs.</p>"""
    replication_server_instance_type: NotRequired[
        "capo_mgn.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>Replication Configuration Replication Server instance type.</p>"""
    use_dedicated_replication_server: NotRequired["bool"]
    """<p>Replication Configuration use Dedicated Replication Server.</p>"""
    default_large_staging_disk_type: NotRequired[
        "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
    ]
    """<p>Replication Configuration use default large Staging Disks.</p>"""
    replicated_disks: NotRequired[
        "capo_mgn.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
    ]
    """<p>Replication Configuration replicated disks.</p>"""
    ebs_encryption: NotRequired[
        "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
    ]
    """<p>Replication Configuration EBS encryption.</p>"""
    ebs_encryption_key_arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>Replication Configuration EBS encryption key ARN.</p>"""
    bandwidth_throttling: "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
    """<p>Replication Configuration set bandwidth throttling.</p>"""
    data_plane_routing: NotRequired[
        "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
    ]
    """<p>Replication Configuration data plane routing.</p>"""
    create_public_ip: NotRequired["bool"]
    """<p>Replication Configuration create Public IP.</p>"""
    staging_area_tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Replication Configuration Staging Area tags.</p>"""
    use_fips_endpoint: NotRequired["bool"]
    """<p>Replication Configuration use Fips Endpoint.</p>"""
    internet_protocol: NotRequired["capo_mgn.types.internet_protocol.InternetProtocol"]
    """<p>Replication Configuration internet protocol.</p>"""
    store_snapshot_on_local_zone: NotRequired["bool"]
    """<p>Replication Configuration store snapshot on local zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfiguration) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "name" in value:
        out["name"] = value["name"]
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
    if "replicated_disks" in value:
        import capo_mgn.types.replication_configuration_replicated_disks

        out["replicatedDisks"] = (
            capo_mgn.types.replication_configuration_replicated_disks.serialize_json(
                value["replicated_disks"]
            )
        )
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


def deserialize_json(data: dict) -> ReplicationConfiguration:
    out: ReplicationConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    if "name" in data:
        out["name"] = data["name"]
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
    if "replicatedDisks" in data:
        import capo_mgn.types.replication_configuration_replicated_disks

        out["replicated_disks"] = (
            capo_mgn.types.replication_configuration_replicated_disks.deserialize_json(
                data["replicatedDisks"]
            )
        )
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
