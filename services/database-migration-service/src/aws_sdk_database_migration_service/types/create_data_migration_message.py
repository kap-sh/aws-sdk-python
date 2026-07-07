"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateDataMigrationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.migration_type_value
    import aws_sdk_database_migration_service.types.secret_string
    import aws_sdk_database_migration_service.types.source_data_settings
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.tag_list
    import aws_sdk_database_migration_service.types.target_data_settings


class CreateDataMigrationMessage(TypedDict, closed=True):
    data_migration_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>A user-friendly name for the data migration. Data migration names have the following constraints:</p> <ul> <li> <p>Must begin with a letter, and can only contain ASCII letters, digits, and hyphens. </p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Length must be from 1 to 255 characters.</p> </li> </ul>"""
    migration_project_identifier: (
        "aws_sdk_database_migration_service.types.string.String"
    )
    """<p>An identifier for the migration project.</p>"""
    data_migration_type: "aws_sdk_database_migration_service.types.migration_type_value.MigrationTypeValue"
    """<p>Specifies if the data migration is full-load only, change data capture (CDC) only, or full-load and CDC.</p>"""
    service_access_role_arn: "aws_sdk_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) for the service access role that you want to use to create the data migration.</p>"""
    enable_cloudwatch_logs: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to enable CloudWatch logs for the data migration.</p>"""
    source_data_settings: NotRequired[
        "aws_sdk_database_migration_service.types.source_data_settings.SourceDataSettings"
    ]
    """<p>Specifies information about the source data provider.</p>"""
    target_data_settings: NotRequired[
        "aws_sdk_database_migration_service.types.target_data_settings.TargetDataSettings"
    ]
    """<p>Specifies information about the target data provider.</p>"""
    number_of_jobs: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.</p>"""
    tags: NotRequired["aws_sdk_database_migration_service.types.tag_list.TagList"]
    """<p>One or more tags to be assigned to the data migration.</p>"""
    selection_rules: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>An optional JSON string specifying what tables, views, and schemas to include or exclude from the migration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataMigrationMessage) -> dict:
    out: dict = {}
    if "data_migration_name" in value:
        out["DataMigrationName"] = value["data_migration_name"]
    out["MigrationProjectIdentifier"] = value["migration_project_identifier"]
    import aws_sdk_database_migration_service.types.migration_type_value

    out["DataMigrationType"] = (
        aws_sdk_database_migration_service.types.migration_type_value.serialize_aws_json_1_1(
            value["data_migration_type"]
        )
    )
    out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    if "enable_cloudwatch_logs" in value:
        out["EnableCloudwatchLogs"] = value["enable_cloudwatch_logs"]
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
    if "tags" in value:
        import aws_sdk_database_migration_service.types.tag_list

        out["Tags"] = (
            aws_sdk_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    if "selection_rules" in value:
        out["SelectionRules"] = value["selection_rules"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataMigrationMessage:
    out: CreateDataMigrationMessage = {}  # type: ignore[typeddict-item]
    if "DataMigrationName" in data:
        out["data_migration_name"] = data["DataMigrationName"]
    if "MigrationProjectIdentifier" in data:
        out["migration_project_identifier"] = data["MigrationProjectIdentifier"]
    else:
        raise DeserializationError(
            "CreateDataMigrationMessage.migration_project_identifier required"
        )
    if "DataMigrationType" in data:
        import aws_sdk_database_migration_service.types.migration_type_value

        out["data_migration_type"] = (
            aws_sdk_database_migration_service.types.migration_type_value.deserialize_aws_json_1_1(
                data["DataMigrationType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataMigrationMessage.data_migration_type required"
        )
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    else:
        raise DeserializationError(
            "CreateDataMigrationMessage.service_access_role_arn required"
        )
    if "EnableCloudwatchLogs" in data:
        out["enable_cloudwatch_logs"] = data["EnableCloudwatchLogs"]
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
    if "Tags" in data:
        import aws_sdk_database_migration_service.types.tag_list

        out["tags"] = (
            aws_sdk_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    if "SelectionRules" in data:
        out["selection_rules"] = data["SelectionRules"]
    return out
