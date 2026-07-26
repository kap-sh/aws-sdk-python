"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRdsDbPendingModifiedValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_rds_db_processor_features
    import capo_securityhub.types.aws_rds_pending_cloud_watch_logs_exports
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsRdsDbPendingModifiedValues(TypedDict, closed=True):
    db_instance_class: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The new DB instance class for the DB instance.</p>"""
    allocated_storage: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The new value of the allocated storage for the DB instance.</p>"""
    master_user_password: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The new master user password for the DB instance.</p>"""
    port: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The new port for the DB instance.</p>"""
    backup_retention_period: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The new backup retention period for the DB instance.</p>"""
    multi_az: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates that a single Availability Zone DB instance is changing to a multiple Availability Zone deployment.</p>"""
    engine_version: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The new engine version for the DB instance.</p>"""
    license_model: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The new license model value for the DB instance.</p>"""
    iops: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The new provisioned IOPS value for the DB instance.</p>"""
    db_instance_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The new DB instance identifier for the DB instance.</p>"""
    storage_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The new storage type for the DB instance.</p>"""
    ca_certificate_identifier: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The new CA certificate identifier for the DB instance.</p>"""
    db_subnet_group_name: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the new subnet group for the DB instance.</p>"""
    pending_cloud_watch_logs_exports: NotRequired[
        "capo_securityhub.types.aws_rds_pending_cloud_watch_logs_exports.AwsRdsPendingCloudWatchLogsExports"
    ]
    """<p>A list of log types that are being enabled or disabled.</p>"""
    processor_features: NotRequired[
        "capo_securityhub.types.aws_rds_db_processor_features.AwsRdsDbProcessorFeatures"
    ]
    """<p>Processor features that are being updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsRdsDbPendingModifiedValues) -> dict:
    out: dict = {}
    if "db_instance_class" in value:
        out["DbInstanceClass"] = value["db_instance_class"]
    if "allocated_storage" in value:
        out["AllocatedStorage"] = value["allocated_storage"]
    if "master_user_password" in value:
        out["MasterUserPassword"] = value["master_user_password"]
    if "port" in value:
        out["Port"] = value["port"]
    if "backup_retention_period" in value:
        out["BackupRetentionPeriod"] = value["backup_retention_period"]
    if "multi_az" in value:
        out["MultiAZ"] = value["multi_az"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "license_model" in value:
        out["LicenseModel"] = value["license_model"]
    if "iops" in value:
        out["Iops"] = value["iops"]
    if "db_instance_identifier" in value:
        out["DbInstanceIdentifier"] = value["db_instance_identifier"]
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    if "ca_certificate_identifier" in value:
        out["CaCertificateIdentifier"] = value["ca_certificate_identifier"]
    if "db_subnet_group_name" in value:
        out["DbSubnetGroupName"] = value["db_subnet_group_name"]
    if "pending_cloud_watch_logs_exports" in value:
        import capo_securityhub.types.aws_rds_pending_cloud_watch_logs_exports

        out["PendingCloudWatchLogsExports"] = (
            capo_securityhub.types.aws_rds_pending_cloud_watch_logs_exports.serialize_json(
                value["pending_cloud_watch_logs_exports"]
            )
        )
    if "processor_features" in value:
        import capo_securityhub.types.aws_rds_db_processor_features

        out["ProcessorFeatures"] = (
            capo_securityhub.types.aws_rds_db_processor_features.serialize_json(
                value["processor_features"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsRdsDbPendingModifiedValues:
    out: AwsRdsDbPendingModifiedValues = {}  # type: ignore[typeddict-item]
    if "DbInstanceClass" in data:
        out["db_instance_class"] = data["DbInstanceClass"]
    if "AllocatedStorage" in data:
        out["allocated_storage"] = data["AllocatedStorage"]
    if "MasterUserPassword" in data:
        out["master_user_password"] = data["MasterUserPassword"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "BackupRetentionPeriod" in data:
        out["backup_retention_period"] = data["BackupRetentionPeriod"]
    if "MultiAZ" in data:
        out["multi_az"] = data["MultiAZ"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "LicenseModel" in data:
        out["license_model"] = data["LicenseModel"]
    if "Iops" in data:
        out["iops"] = data["Iops"]
    if "DbInstanceIdentifier" in data:
        out["db_instance_identifier"] = data["DbInstanceIdentifier"]
    if "StorageType" in data:
        out["storage_type"] = data["StorageType"]
    if "CaCertificateIdentifier" in data:
        out["ca_certificate_identifier"] = data["CaCertificateIdentifier"]
    if "DbSubnetGroupName" in data:
        out["db_subnet_group_name"] = data["DbSubnetGroupName"]
    if "PendingCloudWatchLogsExports" in data:
        import capo_securityhub.types.aws_rds_pending_cloud_watch_logs_exports

        out["pending_cloud_watch_logs_exports"] = (
            capo_securityhub.types.aws_rds_pending_cloud_watch_logs_exports.deserialize_json(
                data["PendingCloudWatchLogsExports"]
            )
        )
    if "ProcessorFeatures" in data:
        import capo_securityhub.types.aws_rds_db_processor_features

        out["processor_features"] = (
            capo_securityhub.types.aws_rds_db_processor_features.deserialize_json(
                data["ProcessorFeatures"]
            )
        )
    return out
