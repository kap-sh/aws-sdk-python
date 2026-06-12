"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyDataMigrationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.migration_type_value
    import aws_sdk_database_migration_service.types.secret_string
    import aws_sdk_database_migration_service.types.source_data_settings
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.target_data_settings


class ModifyDataMigrationMessage(TypedDict):
    data_migration_identifier: "aws_sdk_database_migration_service.types.string.String"
    """<p>The identifier (name or ARN) of the data migration to modify.</p>"""
    data_migration_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The new name for the data migration.</p>"""
    enable_cloudwatch_logs: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Whether to enable Cloudwatch logs for the data migration.</p>"""
    service_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The new service access role ARN for the data migration.</p>"""
    data_migration_type: NotRequired[
        "aws_sdk_database_migration_service.types.migration_type_value.MigrationTypeValue"
    ]
    """<p>The new migration type for the data migration.</p>"""
    source_data_settings: NotRequired[
        "aws_sdk_database_migration_service.types.source_data_settings.SourceDataSettings"
    ]
    """<p>The new information about the source data provider for the data migration.</p>"""
    target_data_settings: NotRequired[
        "aws_sdk_database_migration_service.types.target_data_settings.TargetDataSettings"
    ]
    """<p>The new information about the target data provider for the data migration.</p>"""
    number_of_jobs: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.</p>"""
    selection_rules: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>A JSON-formatted string that defines what objects to include and exclude from the migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyDataMigrationMessage) -> dict:
    out: dict = {}
    out["DataMigrationIdentifier"] = value["data_migration_identifier"]
    if "data_migration_name" in value:
        out["DataMigrationName"] = value["data_migration_name"]
    if "enable_cloudwatch_logs" in value:
        out["EnableCloudwatchLogs"] = value["enable_cloudwatch_logs"]
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "data_migration_type" in value:
        import aws_sdk_database_migration_service.types.migration_type_value

        out["DataMigrationType"] = (
            aws_sdk_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
                value["data_migration_type"]
            )
        )
    if "source_data_settings" in value:
        import aws_sdk_database_migration_service.types.source_data_settings

        out["SourceDataSettings"] = (
            aws_sdk_database_migration_service.types.source_data_settings.serialize_aws_json_1_1(
                value["source_data_settings"]
            )
        )
    if "target_data_settings" in value:
        import aws_sdk_database_migration_service.types.target_data_settings

        out["TargetDataSettings"] = (
            aws_sdk_database_migration_service.types.target_data_settings.serialize_aws_json_1_1(
                value["target_data_settings"]
            )
        )
    if "number_of_jobs" in value:
        out["NumberOfJobs"] = value["number_of_jobs"]
    if "selection_rules" in value:
        out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyDataMigrationMessage:
    out: ModifyDataMigrationMessage = {}  # type: ignore[typeddict-item]
    if "DataMigrationIdentifier" in data:
        out["data_migration_identifier"] = data["DataMigrationIdentifier"]
    else:
        raise DeserializationError(
            "ModifyDataMigrationMessage.data_migration_identifier required"
        )
    if "DataMigrationName" in data:
        out["data_migration_name"] = data["DataMigrationName"]
    if "EnableCloudwatchLogs" in data:
        out["enable_cloudwatch_logs"] = data["EnableCloudwatchLogs"]
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if "DataMigrationType" in data:
        import aws_sdk_database_migration_service.types.migration_type_value

        out["data_migration_type"] = (
            aws_sdk_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["DataMigrationType"]
            )
        )
    if "SourceDataSettings" in data:
        import aws_sdk_database_migration_service.types.source_data_settings

        out["source_data_settings"] = (
            aws_sdk_database_migration_service.types.source_data_settings.deserialize_aws_json_1_1(
                data["SourceDataSettings"]
            )
        )
    if "TargetDataSettings" in data:
        import aws_sdk_database_migration_service.types.target_data_settings

        out["target_data_settings"] = (
            aws_sdk_database_migration_service.types.target_data_settings.deserialize_aws_json_1_1(
                data["TargetDataSettings"]
            )
        )
    if "NumberOfJobs" in data:
        out["number_of_jobs"] = data["NumberOfJobs"]
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    return out
