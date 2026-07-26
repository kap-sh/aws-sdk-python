"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReplicationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.compute_config
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class ReplicationConfig(TypedDict, closed=True):
    replication_config_identifier: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The identifier for the <code>ReplicationConfig</code> associated with the replication.</p>"""
    replication_config_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of this DMS Serverless replication configuration.</p>"""
    source_endpoint_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the source endpoint for this DMS serverless replication configuration.</p>"""
    target_endpoint_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration.</p>"""
    replication_type: NotRequired[
        "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The type of the replication.</p>"""
    compute_config: NotRequired[
        "capo_database_migration_service.types.compute_config.ComputeConfig"
    ]
    """<p>Configuration parameters for provisioning an DMS serverless replication.</p>"""
    replication_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Configuration parameters for an DMS serverless replication.</p>"""
    supplemental_settings: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>Additional parameters for an DMS serverless replication.</p>"""
    table_mappings: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>Table mappings specified in the replication.</p>"""
    replication_config_create_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time the serverless replication config was created.</p>"""
    replication_config_update_time: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The time the serverless replication config was updated.</p>"""
    is_read_only: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the replication configuration is read-only. When set to <code>true</code>, this replication configuration is managed by DMS as part of a zero-ETL integration and cannot be modified or deleted directly. You can only modify or delete read-only replication configurations through their associated zero-ETL integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationConfig) -> dict:
    out: dict = {}
    if "replication_config_identifier" in value:
        out["ReplicationConfigIdentifier"] = value["replication_config_identifier"]
    if "replication_config_arn" in value:
        out["ReplicationConfigArn"] = value["replication_config_arn"]
    if "source_endpoint_arn" in value:
        out["SourceEndpointArn"] = value["source_endpoint_arn"]
    if "target_endpoint_arn" in value:
        out["TargetEndpointArn"] = value["target_endpoint_arn"]
    if "replication_type" in value:
        import capo_database_migration_service.types.migration_type_value

        out["ReplicationType"] = (
            capo_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["replication_type"]
            )
        )
    if "compute_config" in value:
        import capo_database_migration_service.types.compute_config

        out["ComputeConfig"] = (
            capo_database_migration_service.types.compute_config.serialize_aws_json_1_1(
                value["compute_config"]
            )
        )
    if "replication_settings" in value:
        out["ReplicationSettings"] = value["replication_settings"]
    if "supplemental_settings" in value:
        out["SupplementalSettings"] = value["supplemental_settings"]
    if "table_mappings" in value:
        out["TableMappings"] = value["table_mappings"]
    if "replication_config_create_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationConfigCreateTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_config_create_time"]
            )
        )
    if "replication_config_update_time" in value:
        import capo_database_migration_service.types.t_stamp

        out["ReplicationConfigUpdateTime"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["replication_config_update_time"]
            )
        )
    if "is_read_only" in value:
        out["IsReadOnly"] = value["is_read_only"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicationConfig:
    out: ReplicationConfig = {}  # type: ignore[typeddict-item]
    if "ReplicationConfigIdentifier" in data:
        out["replication_config_identifier"] = data["ReplicationConfigIdentifier"]
    if "ReplicationConfigArn" in data:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    if "SourceEndpointArn" in data:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    if "TargetEndpointArn" in data:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    if "ReplicationType" in data:
        import capo_database_migration_service.types.migration_type_value

        out["replication_type"] = (
            capo_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["ReplicationType"]
            )
        )
    if "ComputeConfig" in data:
        import capo_database_migration_service.types.compute_config

        out["compute_config"] = (
            capo_database_migration_service.types.compute_config.deserialize_aws_json_1_1(
                data["ComputeConfig"]
            )
        )
    if "ReplicationSettings" in data:
        out["replication_settings"] = data["ReplicationSettings"]
    if "SupplementalSettings" in data:
        out["supplemental_settings"] = data["SupplementalSettings"]
    if "TableMappings" in data:
        out["table_mappings"] = data["TableMappings"]
    if "ReplicationConfigCreateTime" in data:
        import capo_database_migration_service.types.t_stamp

        out["replication_config_create_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationConfigCreateTime"]
            )
        )
    if "ReplicationConfigUpdateTime" in data:
        import capo_database_migration_service.types.t_stamp

        out["replication_config_update_time"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ReplicationConfigUpdateTime"]
            )
        )
    if "IsReadOnly" in data:
        out["is_read_only"] = data["IsReadOnly"]
    return out
