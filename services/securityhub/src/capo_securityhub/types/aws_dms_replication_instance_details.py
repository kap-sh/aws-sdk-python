"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDmsReplicationInstanceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_dms_replication_instance_replication_subnet_group_details
    import capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsDmsReplicationInstanceDetails(TypedDict, closed=True):
    allocated_storage: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The amount of storage (in gigabytes) that is allocated for the replication instance. </p>"""
    auto_minor_version_upgrade: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. </p>"""
    availability_zone: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Availability Zone that the replication instance is created in. The default value is a random, system-chosen Availability Zone in the endpoint's Amazon Web Services Region, such as <code>us-east-1d</code>.</p>"""
    engine_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The engine version number of the replication instance. If an engine version number is not specified when a replication instance is created, the default is the latest engine version available. </p>"""
    kms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> An KMS key identifier that is used to encrypt the data on the replication instance. If you don't specify a value for the <code>KmsKeyId</code> parameter, DMS uses your default encryption key. KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""
    multi_az: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Specifies whether the replication instance is deployed across multiple Availability Zones (AZs). You can't set the <code>AvailabilityZone</code> parameter if the <code>MultiAZ</code> parameter is set to <code>true</code>.</p>"""
    preferred_maintenance_window: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The maintenance window times for the replication instance. Upgrades to the replication instance are performed during this time.</p>"""
    publicly_accessible: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p> Specifies the accessibility options for the replication instance. A value of <code>true</code> represents an instance with a public IP address. A value of <code>false</code> represents an instance with a private IP address. The default value is <code>true</code>.</p>"""
    replication_instance_class: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The compute and memory capacity of the replication instance as defined for the specified replication instance class. </p>"""
    replication_instance_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The replication instance identifier.</p>"""
    replication_subnet_group: NotRequired[
        "capo_securityhub.types.aws_dms_replication_instance_replication_subnet_group_details.AwsDmsReplicationInstanceReplicationSubnetGroupDetails"
    ]
    """<p> The subnet group for the replication instance.</p>"""
    vpc_security_groups: NotRequired[
        "capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_list.AwsDmsReplicationInstanceVpcSecurityGroupsList"
    ]
    """<p> The virtual private cloud (VPC) security group for the replication instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDmsReplicationInstanceDetails) -> dict:
    out: dict = {}
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "multi_az" in value:
        out["MultiAZ"] = value["multi_az"]
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    if "replication_instance_class" in value:
        out["ReplicationInstanceClass"] = value["replication_instance_class"]
    if "replication_instance_identifier" in value:
        out["ReplicationInstanceIdentifier"] = value["replication_instance_identifier"]
    if "replication_subnet_group" in value:
        import capo_securityhub.types.aws_dms_replication_instance_replication_subnet_group_details

        out["ReplicationSubnetGroup"] = (
            capo_securityhub.types.aws_dms_replication_instance_replication_subnet_group_details.serialize_json(
                value["replication_subnet_group"]
            )
        )
    if "vpc_security_groups" in value:
        import capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_list

        out["VpcSecurityGroups"] = (
            capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_list.serialize_json(
                value["vpc_security_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsDmsReplicationInstanceDetails:
    out: AwsDmsReplicationInstanceDetails = {}  # type: ignore[typeddict-item]
    if "AllocatedStorage" in data:
        out["allocated_storage"] = data["AllocatedStorage"]
    if "AutoMinorVersionUpgrade" in data:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "MultiAZ" in data:
        out["multi_az"] = data["MultiAZ"]
    if "PreferredMaintenanceWindow" in data:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if "PubliclyAccessible" in data:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    if "ReplicationInstanceClass" in data:
        out["replication_instance_class"] = data["ReplicationInstanceClass"]
    if "ReplicationInstanceIdentifier" in data:
        out["replication_instance_identifier"] = data["ReplicationInstanceIdentifier"]
    if "ReplicationSubnetGroup" in data:
        import capo_securityhub.types.aws_dms_replication_instance_replication_subnet_group_details

        out["replication_subnet_group"] = (
            capo_securityhub.types.aws_dms_replication_instance_replication_subnet_group_details.deserialize_json(
                data["ReplicationSubnetGroup"]
            )
        )
    if "VpcSecurityGroups" in data:
        import capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_list

        out["vpc_security_groups"] = (
            capo_securityhub.types.aws_dms_replication_instance_vpc_security_groups_list.deserialize_json(
                data["VpcSecurityGroups"]
            )
        )
    return out
