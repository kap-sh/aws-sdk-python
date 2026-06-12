"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#InstanceProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.iso8601_date_time
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.string_list


class InstanceProfile(TypedDict):
    instance_profile_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the instance profile.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Availability Zone where the instance profile runs.</p>"""
    kms_key_arn: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that is used to encrypt the connection parameters for the instance profile.</p> <p>If you don't specify a value for the <code>KmsKeyArn</code> parameter, then DMS uses an Amazon Web Services owned encryption key to encrypt your resources.</p>"""
    publicly_accessible: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies the accessibility options for the instance profile. A value of <code>true</code> represents an instance profile with a public IP address. A value of <code>false</code> represents an instance profile with a private IP address. The default value is <code>true</code>.</p>"""
    network_type: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Specifies the network type for the instance profile. A value of <code>IPV4</code> represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of <code>IPV6</code> represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of <code>DUAL</code> represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.</p>"""
    instance_profile_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The user-friendly name for the instance profile.</p>"""
    description: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A description of the instance profile. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.</p>"""
    instance_profile_creation_time: NotRequired[
        "aws_sdk_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The time the instance profile was created.</p>"""
    subnet_group_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The identifier of the subnet group that is associated with the instance profile.</p>"""
    vpc_security_groups: NotRequired[
        "aws_sdk_database_migration_service.types.string_list.StringList"
    ]
    """<p>The VPC security groups that are used with the instance profile. The VPC security group must work with the VPC containing the instance profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceProfile) -> dict:
    out: dict = {}
    if "instance_profile_arn" in value:
        out["InstanceProfileArn"] = value["instance_profile_arn"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "publicly_accessible" in value:
        out["PubliclyAccessible"] = value["publicly_accessible"]
    if "network_type" in value:
        out["NetworkType"] = value["network_type"]
    if "instance_profile_name" in value:
        out["InstanceProfileName"] = value["instance_profile_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "instance_profile_creation_time" in value:
        import aws_sdk_database_migration_service.types.iso8601_date_time

        out["InstanceProfileCreationTime"] = (
            aws_sdk_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["instance_profile_creation_time"]
            )
        )
    if "subnet_group_identifier" in value:
        out["SubnetGroupIdentifier"] = value["subnet_group_identifier"]
    if "vpc_security_groups" in value:
        import aws_sdk_database_migration_service.types.string_list

        out["VpcSecurityGroups"] = (
            aws_sdk_database_migration_service.types.string_list.serialize_aws_json_1_1(
                value["vpc_security_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceProfile:
    out: InstanceProfile = {}  # type: ignore[typeddict-item]
    if "InstanceProfileArn" in data:
        out["instance_profile_arn"] = data["InstanceProfileArn"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "PubliclyAccessible" in data:
        out["publicly_accessible"] = data["PubliclyAccessible"]
    if "NetworkType" in data:
        out["network_type"] = data["NetworkType"]
    if "InstanceProfileName" in data:
        out["instance_profile_name"] = data["InstanceProfileName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "InstanceProfileCreationTime" in data:
        import aws_sdk_database_migration_service.types.iso8601_date_time

        out["instance_profile_creation_time"] = (
            aws_sdk_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["InstanceProfileCreationTime"]
            )
        )
    if "SubnetGroupIdentifier" in data:
        out["subnet_group_identifier"] = data["SubnetGroupIdentifier"]
    if "VpcSecurityGroups" in data:
        import aws_sdk_database_migration_service.types.string_list

        out["vpc_security_groups"] = (
            aws_sdk_database_migration_service.types.string_list.deserialize_aws_json_1_1(
                data["VpcSecurityGroups"]
            )
        )
    return out
