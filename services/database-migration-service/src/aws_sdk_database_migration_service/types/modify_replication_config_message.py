"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyReplicationConfigMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.compute_config
    import aws_sdk_database_migration_service.types.migration_type_value
    import aws_sdk_database_migration_service.types.string


class ModifyReplicationConfigMessage(TypedDict):
    replication_config_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name of the replication to modify.</p>"""
    replication_config_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The new replication config to apply to the replication.</p>"""
    replication_type: NotRequired[
        "aws_sdk_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The type of replication.</p>"""
    table_mappings: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Table mappings specified in the replication.</p>"""
    replication_settings: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The settings for the replication.</p>"""
    supplemental_settings: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Additional settings for the replication.</p>"""
    compute_config: NotRequired[
        "aws_sdk_database_migration_service.types.compute_config.ComputeConfig"
    ]
    """<p>Configuration parameters for provisioning an DMS Serverless replication.</p>"""
    source_endpoint_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the source endpoint for this DMS serverless replication configuration.</p>"""
    target_endpoint_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyReplicationConfigMessage) -> dict:
    out: dict = {}
    out["ReplicationConfigArn"] = value["replication_config_arn"]
    if "replication_config_identifier" in value:
        out["ReplicationConfigIdentifier"] = value["replication_config_identifier"]
    if "replication_type" in value:
        import aws_sdk_database_migration_service.types.migration_type_value

        out["ReplicationType"] = (
            aws_sdk_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["replication_type"]
            )
        )
    if "table_mappings" in value:
        out["TableMappings"] = value["table_mappings"]
    if "replication_settings" in value:
        out["ReplicationSettings"] = value["replication_settings"]
    if "supplemental_settings" in value:
        out["SupplementalSettings"] = value["supplemental_settings"]
    if "compute_config" in value:
        import aws_sdk_database_migration_service.types.compute_config

        out["ComputeConfig"] = (
            aws_sdk_database_migration_service.types.compute_config.serialize_aws_json_1_1(
                value["compute_config"]
            )
        )
    if "source_endpoint_arn" in value:
        out["SourceEndpointArn"] = value["source_endpoint_arn"]
    if "target_endpoint_arn" in value:
        out["TargetEndpointArn"] = value["target_endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyReplicationConfigMessage:
    out: ModifyReplicationConfigMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationConfigArn" in data:
        out["replication_config_arn"] = data["ReplicationConfigArn"]
    else:
        raise DeserializationError(
            "ModifyReplicationConfigMessage.replication_config_arn required"
        )
    if "ReplicationConfigIdentifier" in data:
        out["replication_config_identifier"] = data["ReplicationConfigIdentifier"]
    if "ReplicationType" in data:
        import aws_sdk_database_migration_service.types.migration_type_value

        out["replication_type"] = (
            aws_sdk_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["ReplicationType"]
            )
        )
    if "TableMappings" in data:
        out["table_mappings"] = data["TableMappings"]
    if "ReplicationSettings" in data:
        out["replication_settings"] = data["ReplicationSettings"]
    if "SupplementalSettings" in data:
        out["supplemental_settings"] = data["SupplementalSettings"]
    if "ComputeConfig" in data:
        import aws_sdk_database_migration_service.types.compute_config

        out["compute_config"] = (
            aws_sdk_database_migration_service.types.compute_config.deserialize_aws_json_1_1(
                data["ComputeConfig"]
            )
        )
    if "SourceEndpointArn" in data:
        out["source_endpoint_arn"] = data["SourceEndpointArn"]
    if "TargetEndpointArn" in data:
        out["target_endpoint_arn"] = data["TargetEndpointArn"]
    return out
