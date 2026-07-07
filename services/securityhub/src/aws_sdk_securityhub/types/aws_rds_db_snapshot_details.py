"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbSnapshotDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_rds_db_processor_features
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsRdsDbSnapshotDetails(TypedDict, closed=True):
    db_snapshot_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name or ARN of the DB snapshot that is used to restore the DB instance.</p>"""
    db_instance_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A name for the DB instance.</p>"""
    snapshot_create_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>When the snapshot was taken in Coordinated Universal Time (UTC).</p>"""
    engine: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the database engine to use for this DB instance. Valid values are as follows:</p> <ul> <li> <p> <code>aurora</code> </p> </li> <li> <p> <code>aurora-mysql</code> </p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>c</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-se</code> </p> </li> <li> <p> <code>oracle-se1</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>"""
    allocated_storage: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The amount of storage (in gigabytes) to be initially allocated for the database instance.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of this DB snapshot.</p>"""
    port: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The port that the database engine was listening on at the time of the snapshot.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the name of the Availability Zone in which the DB instance was located at the time of the DB snapshot.</p>"""
    vpc_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The VPC ID associated with the DB snapshot.</p>"""
    instance_create_time: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the time in Coordinated Universal Time (UTC) when the DB instance, from which the snapshot was taken, was created.</p>"""
    master_username: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The master user name for the DB snapshot.</p>"""
    engine_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the database engine.</p>"""
    license_model: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>License model information for the restored DB instance.</p>"""
    snapshot_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The type of the DB snapshot.</p>"""
    iops: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The provisioned IOPS (I/O operations per second) value of the DB instance at the time of the snapshot.</p>"""
    option_group_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The option group name for the DB snapshot.</p>"""
    percent_progress: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The percentage of the estimated data that has been transferred.</p>"""
    source_region: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services Region that the DB snapshot was created in or copied from.</p>"""
    source_db_snapshot_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The DB snapshot ARN that the DB snapshot was copied from.</p>"""
    storage_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The storage type associated with the DB snapshot. Valid values are as follows:</p> <ul> <li> <p> <code>gp2</code> </p> </li> <li> <p> <code>io1</code> </p> </li> <li> <p> <code>standard</code> </p> </li> </ul>"""
    tde_credential_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN from the key store with which to associate the instance for TDE encryption.</p>"""
    encrypted: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the DB snapshot is encrypted.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>If <code>Encrypted</code> is <code>true</code>, the KMS key identifier for the encrypted DB snapshot.</p>"""
    timezone: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The time zone of the DB snapshot.</p>"""
    iam_database_authentication_enabled: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether mapping of IAM accounts to database accounts is enabled.</p>"""
    processor_features: NotRequired[
        "aws_sdk_securityhub.types.aws_rds_db_processor_features.AwsRdsDbProcessorFeatures"
    ]
    """<p>The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.</p>"""
    dbi_resource_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier for the source DB instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbSnapshotDetails) -> dict:
    out: dict = {}
    if "db_snapshot_identifier" in value:
        out["DbSnapshotIdentifier"] = value["db_snapshot_identifier"]
    if "db_instance_identifier" in value:
        out["DbInstanceIdentifier"] = value["db_instance_identifier"]
    if "snapshot_create_time" in value:
        out["SnapshotCreateTime"] = value["snapshot_create_time"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    if "status" in value:
        out["Status"] = value["status"]
    if "port" in value:
        out["Port"] = value["port"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "instance_create_time" in value:
        out["InstanceCreateTime"] = value["instance_create_time"]
    if "master_username" in value:
        out["MasterUsername"] = value["master_username"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "license_model" in value:
        out["LicenseModel"] = value["license_model"]
    if "snapshot_type" in value:
        out["SnapshotType"] = value["snapshot_type"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "option_group_name" in value:
        out["OptionGroupName"] = value["option_group_name"]
    if "percent_progress" in value:
        out["PercentProgress"] = value["percent_progress"]
    if "source_region" in value:
        out["SourceRegion"] = value["source_region"]
    if "source_db_snapshot_identifier" in value:
        out["SourceDbSnapshotIdentifier"] = value["source_db_snapshot_identifier"]
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    if "tde_credential_arn" in value:
        out["TdeCredentialArn"] = value["tde_credential_arn"]
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "iam_database_authentication_enabled" in value:
        out["IamDatabaseAuthenticationEnabled"] = value[
            "iam_database_authentication_enabled"
        ]
    if "processor_features" in value:
        import aws_sdk_securityhub.types.aws_rds_db_processor_features

        out["ProcessorFeatures"] = (
            aws_sdk_securityhub.types.aws_rds_db_processor_features.serialize_json(
                value["processor_features"]
            )
        )
    if "dbi_resource_id" in value:
        out["DbiResourceId"] = value["dbi_resource_id"]
    return out


def deserialize_json(data: dict) -> AwsRdsDbSnapshotDetails:
    out: AwsRdsDbSnapshotDetails = {}  # type: ignore[typeddict-item]
    if "DbSnapshotIdentifier" in data:
        out["db_snapshot_identifier"] = data["DbSnapshotIdentifier"]
    if "DbInstanceIdentifier" in data:
        out["db_instance_identifier"] = data["DbInstanceIdentifier"]
    if "SnapshotCreateTime" in data:
        out["snapshot_create_time"] = data["SnapshotCreateTime"]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "AllocatedStorage" in data:
        out["allocated_storage"] = data["AllocatedStorage"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "InstanceCreateTime" in data:
        out["instance_create_time"] = data["InstanceCreateTime"]
    if "MasterUsername" in data:
        out["master_username"] = data["MasterUsername"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "LicenseModel" in data:
        out["license_model"] = data["LicenseModel"]
    if "SnapshotType" in data:
        out["snapshot_type"] = data["SnapshotType"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "OptionGroupName" in data:
        out["option_group_name"] = data["OptionGroupName"]
    if "PercentProgress" in data:
        out["percent_progress"] = data["PercentProgress"]
    if "SourceRegion" in data:
        out["source_region"] = data["SourceRegion"]
    if "SourceDbSnapshotIdentifier" in data:
        out["source_db_snapshot_identifier"] = data["SourceDbSnapshotIdentifier"]
    if "StorageType" in data:
        out["storage_type"] = data["StorageType"]
    if "TdeCredentialArn" in data:
        out["tde_credential_arn"] = data["TdeCredentialArn"]
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "IamDatabaseAuthenticationEnabled" in data:
        out["iam_database_authentication_enabled"] = data[
            "IamDatabaseAuthenticationEnabled"
        ]
    if "ProcessorFeatures" in data:
        import aws_sdk_securityhub.types.aws_rds_db_processor_features

        out["processor_features"] = (
            aws_sdk_securityhub.types.aws_rds_db_processor_features.deserialize_json(
                data["ProcessorFeatures"]
            )
        )
    if "DbiResourceId" in data:
        out["dbi_resource_id"] = data["DbiResourceId"]
    return out
