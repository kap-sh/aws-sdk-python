"""Generated from Smithy shape ``com.amazonaws.drs#ReplicationConfigurationTemplate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.ec2_instance_type
    import aws_sdk_drs.types.internet_protocol
    import aws_sdk_drs.types.pit_policy
    import aws_sdk_drs.types.positive_integer
    import aws_sdk_drs.types.replication_configuration_data_plane_routing
    import aws_sdk_drs.types.replication_configuration_default_large_staging_disk_type
    import aws_sdk_drs.types.replication_configuration_ebs_encryption
    import aws_sdk_drs.types.replication_configuration_template_id
    import aws_sdk_drs.types.replication_servers_security_groups_i_ds
    import aws_sdk_drs.types.subnet_id
    import aws_sdk_drs.types.tags_map


class ReplicationConfigurationTemplate(TypedDict):
    replication_configuration_template_id: "aws_sdk_drs.types.replication_configuration_template_id.ReplicationConfigurationTemplateID"
    """<p>The Replication Configuration Template ID.</p>"""
    arn: NotRequired["aws_sdk_drs.types.arn.ARN"]
    """<p>The Replication Configuration Template ARN.</p>"""
    staging_area_subnet_id: NotRequired["aws_sdk_drs.types.subnet_id.SubnetID"]
    """<p>The subnet to be used by the replication staging area.</p>"""
    associate_default_security_group: NotRequired["bool"]
    """<p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration Template.</p>"""
    replication_servers_security_groups_i_ds: NotRequired[
        "aws_sdk_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
    ]
    """<p>The security group IDs that will be used by the replication server.</p>"""
    replication_server_instance_type: NotRequired[
        "aws_sdk_drs.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>The instance type to be used for the replication server.</p>"""
    use_dedicated_replication_server: NotRequired["bool"]
    """<p>Whether to use a dedicated Replication Server in the replication staging area.</p>"""
    default_large_staging_disk_type: NotRequired[
        "aws_sdk_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
    ]
    """<p>The Staging Disk EBS volume type to be used during replication.</p>"""
    ebs_encryption: NotRequired[
        "aws_sdk_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
    ]
    """<p>The type of EBS encryption to be used during replication.</p>"""
    ebs_encryption_key_arn: NotRequired["aws_sdk_drs.types.arn.ARN"]
    """<p>The ARN of the EBS encryption key to be used during replication.</p>"""
    bandwidth_throttling: "aws_sdk_drs.types.positive_integer.PositiveInteger"
    """<p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>"""
    data_plane_routing: NotRequired[
        "aws_sdk_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
    ]
    """<p>The data plane routing mechanism that will be used for replication.</p>"""
    create_public_ip: NotRequired["bool"]
    """<p>Whether to create a Public IP for the Recovery Instance by default.</p>"""
    staging_area_tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>"""
    tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>A set of tags to be associated with the Replication Configuration Template resource.</p>"""
    pit_policy: NotRequired["aws_sdk_drs.types.pit_policy.PITPolicy"]
    """<p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>"""
    auto_replicate_new_disks: NotRequired["bool"]
    """<p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>"""
    internet_protocol: NotRequired[
        "aws_sdk_drs.types.internet_protocol.InternetProtocol"
    ]
    """<p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>"""


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
        import aws_sdk_drs.types.replication_servers_security_groups_i_ds

        out["replicationServersSecurityGroupsIDs"] = (
            aws_sdk_drs.types.replication_servers_security_groups_i_ds.serialize_json(
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
        import aws_sdk_drs.types.tags_map

        out["stagingAreaTags"] = aws_sdk_drs.types.tags_map.serialize_json(
            value["staging_area_tags"]
        )
    if "tags" in value:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    if "pit_policy" in value:
        import aws_sdk_drs.types.pit_policy

        out["pitPolicy"] = aws_sdk_drs.types.pit_policy.serialize_json(
            value["pit_policy"]
        )
    if "auto_replicate_new_disks" in value:
        out["autoReplicateNewDisks"] = value["auto_replicate_new_disks"]
    if "internet_protocol" in value:
        out["internetProtocol"] = value["internet_protocol"]
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
        import aws_sdk_drs.types.replication_servers_security_groups_i_ds

        out["replication_servers_security_groups_i_ds"] = (
            aws_sdk_drs.types.replication_servers_security_groups_i_ds.deserialize_json(
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
        import aws_sdk_drs.types.tags_map

        out["staging_area_tags"] = aws_sdk_drs.types.tags_map.deserialize_json(
            data["stagingAreaTags"]
        )
    if "tags" in data:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    if "pitPolicy" in data:
        import aws_sdk_drs.types.pit_policy

        out["pit_policy"] = aws_sdk_drs.types.pit_policy.deserialize_json(
            data["pitPolicy"]
        )
    if "autoReplicateNewDisks" in data:
        out["auto_replicate_new_disks"] = data["autoReplicateNewDisks"]
    if "internetProtocol" in data:
        out["internet_protocol"] = data["internetProtocol"]
    return out
