"""Generated from Smithy shape ``com.amazonaws.mgn#ReplicationConfigurationTemplate``."""

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
    import aws_sdk_mgn.types.replication_configuration_template_id
    import aws_sdk_mgn.types.replication_servers_security_groups_i_ds
    import aws_sdk_mgn.types.subnet_id
    import aws_sdk_mgn.types.tags_map


class ReplicationConfigurationTemplate(TypedDict):
    replication_configuration_template_id: "aws_sdk_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID"
    """<p>Replication Configuration template ID.</p>"""
    arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>Replication Configuration template ARN.</p>"""
    staging_area_subnet_id: NotRequired["aws_sdk_mgn.types.subnet_id.SubnetID"]
    """<p>Replication Configuration template Staging Area subnet ID.</p>"""
    associate_default_security_group: NotRequired["bool"]
    """<p>Replication Configuration template associate default Application Migration Service Security group.</p>"""
    replication_servers_security_groups_i_ds: NotRequired[
        "aws_sdk_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
    ]
    """<p>Replication Configuration template server Security Groups IDs.</p>"""
    replication_server_instance_type: NotRequired[
        "aws_sdk_mgn.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>Replication Configuration template server instance type.</p>"""
    use_dedicated_replication_server: NotRequired["bool"]
    """<p>Replication Configuration template use Dedicated Replication Server.</p>"""
    default_large_staging_disk_type: NotRequired[
        "aws_sdk_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
    ]
    """<p>Replication Configuration template use default large Staging Disk type.</p>"""
    ebs_encryption: NotRequired[
        "aws_sdk_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
    ]
    """<p>Replication Configuration template EBS encryption.</p>"""
    ebs_encryption_key_arn: NotRequired["aws_sdk_mgn.types.arn.ARN"]
    """<p>Replication Configuration template EBS encryption key ARN.</p>"""
    bandwidth_throttling: "aws_sdk_mgn.types.bandwidth_throttling.BandwidthThrottling"
    """<p>Replication Configuration template bandwidth throttling.</p>"""
    data_plane_routing: NotRequired[
        "aws_sdk_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
    ]
    """<p>Replication Configuration template data plane routing.</p>"""
    create_public_ip: NotRequired["bool"]
    """<p>Replication Configuration template create Public IP.</p>"""
    staging_area_tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Replication Configuration template Staging Area Tags.</p>"""
    use_fips_endpoint: NotRequired["bool"]
    """<p>Replication Configuration template use Fips Endpoint.</p>"""
    tags: NotRequired["aws_sdk_mgn.types.tags_map.TagsMap"]
    """<p>Replication Configuration template Tags.</p>"""
    internet_protocol: NotRequired[
        "aws_sdk_mgn.types.internet_protocol.InternetProtocol"
    ]
    """<p>Replication Configuration template internet protocol.</p>"""
    store_snapshot_on_local_zone: NotRequired["bool"]
    """<p>Replication Configuration template store snapshot on local zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationConfigurationTemplate) -> dict:
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
        import aws_sdk_mgn.types.replication_servers_security_groups_i_ds

        out["replicationServersSecurityGroupsIDs"] = (
            aws_sdk_mgn.types.replication_servers_security_groups_i_ds.serialize_json(
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


def deserialize_json(data: dict) -> ReplicationConfigurationTemplate:
    out: ReplicationConfigurationTemplate = {}  # type: ignore[typeddict-item]
    if "replicationConfigurationTemplateID" in data:
        out["replication_configuration_template_id"] = data[
            "replicationConfigurationTemplateID"
        ]
    else:
        raise DeserializationError(
            "ReplicationConfigurationTemplate.replication_configuration_template_id required"
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "stagingAreaSubnetId" in data:
        out["staging_area_subnet_id"] = data["stagingAreaSubnetId"]
    if "associateDefaultSecurityGroup" in data:
        out["associate_default_security_group"] = data["associateDefaultSecurityGroup"]
    if "replicationServersSecurityGroupsIDs" in data:
        import aws_sdk_mgn.types.replication_servers_security_groups_i_ds

        out["replication_servers_security_groups_i_ds"] = (
            aws_sdk_mgn.types.replication_servers_security_groups_i_ds.deserialize_json(
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
        import aws_sdk_mgn.types.tags_map

        out["staging_area_tags"] = aws_sdk_mgn.types.tags_map.deserialize_json(
            data["stagingAreaTags"]
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
