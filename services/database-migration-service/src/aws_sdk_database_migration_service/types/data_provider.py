"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.data_provider_settings
    import aws_sdk_database_migration_service.types.iso8601_date_time
    import aws_sdk_database_migration_service.types.string


class DataProvider(TypedDict, closed=True):
    data_provider_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name of the data provider.</p>"""
    data_provider_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) string that uniquely identifies the data provider.</p>"""
    data_provider_creation_time: NotRequired[
        "aws_sdk_database_migration_service.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The time the data provider was created.</p>"""
    description: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A description of the data provider. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.</p>"""
    engine: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    r"""<p>The type of database engine for the data provider. Valid values include <code>\"aurora\"</code>, <code>\"aurora-postgresql\"</code>, <code>\"mysql\"</code>, <code>\"oracle\"</code>, <code>\"postgres\"</code>, <code>\"sqlserver\"</code>, <code>redshift</code>, <code>mariadb</code>, <code>mongodb</code>, <code>db2</code>, <code>db2-zos</code>, <code>docdb</code>, and <code>sybase</code>. A value of <code>\"aurora\"</code> represents Amazon Aurora MySQL-Compatible Edition.</p>"""
    virtual: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the data provider is virtual.</p>"""
    settings: NotRequired[
        "aws_sdk_database_migration_service.types.data_provider_settings.DataProviderSettings"
    ]
    """<p>The settings in JSON format for a data provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProvider) -> dict:
    out: dict = {}
    if "data_provider_name" in value:
        out["DataProviderName"] = value["data_provider_name"]
    if "data_provider_arn" in value:
        out["DataProviderArn"] = value["data_provider_arn"]
    if "data_provider_creation_time" in value:
        import aws_sdk_database_migration_service.types.iso8601_date_time

        out["DataProviderCreationTime"] = (
            aws_sdk_database_migration_service.types.iso8601_date_time.serialize_aws_json_1_1(
                value["data_provider_creation_time"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "virtual" in value:
        out["Virtual"] = value["virtual"]
    if "settings" in value:
        import aws_sdk_database_migration_service.types.data_provider_settings

        out["Settings"] = (
            aws_sdk_database_migration_service.types.data_provider_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataProvider:
    out: DataProvider = {}  # type: ignore[typeddict-item]
    if "DataProviderName" in data:
        out["data_provider_name"] = data["DataProviderName"]
    if "DataProviderArn" in data:
        out["data_provider_arn"] = data["DataProviderArn"]
    if "DataProviderCreationTime" in data:
        import aws_sdk_database_migration_service.types.iso8601_date_time

        out["data_provider_creation_time"] = (
            aws_sdk_database_migration_service.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["DataProviderCreationTime"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "Virtual" in data:
        out["virtual"] = data["Virtual"]
    if "Settings" in data:
        import aws_sdk_database_migration_service.types.data_provider_settings

        out["settings"] = (
            aws_sdk_database_migration_service.types.data_provider_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
