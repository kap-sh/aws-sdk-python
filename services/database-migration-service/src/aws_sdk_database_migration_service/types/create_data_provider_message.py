"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CreateDataProviderMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.data_provider_settings
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.tag_list


class CreateDataProviderMessage(TypedDict):
    data_provider_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>A user-friendly name for the data provider.</p>"""
    description: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A user-friendly description of the data provider.</p>"""
    engine: "aws_sdk_database_migration_service.types.string.String"
    """<p>The type of database engine for the data provider. Valid values include <code>\"aurora\"</code>, <code>\"aurora-postgresql\"</code>, <code>\"mysql\"</code>, <code>\"oracle\"</code>, <code>\"postgres\"</code>, <code>\"sqlserver\"</code>, <code>redshift</code>, <code>mariadb</code>, <code>mongodb</code>, <code>db2</code>, <code>db2-zos</code>, <code>docdb</code>, and <code>sybase</code>. A value of <code>\"aurora\"</code> represents Amazon Aurora MySQL-Compatible Edition.</p>"""
    virtual: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the data provider is virtual.</p>"""
    settings: "aws_sdk_database_migration_service.types.data_provider_settings.DataProviderSettings"
    """<p>The settings in JSON format for a data provider.</p>"""
    tags: NotRequired["aws_sdk_database_migration_service.types.tag_list.TagList"]
    """<p>One or more tags to be assigned to the data provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDataProviderMessage) -> dict:
    out: dict = {}
    if "data_provider_name" in value:
        out["DataProviderName"] = value["data_provider_name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Engine"] = value["engine"]
    if "virtual" in value:
        out["Virtual"] = value["virtual"]
    import aws_sdk_database_migration_service.types.data_provider_settings

    out["Settings"] = (
        aws_sdk_database_migration_service.types.data_provider_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    )
    if "tags" in value:
        import aws_sdk_database_migration_service.types.tag_list

        out["Tags"] = (
            aws_sdk_database_migration_service.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDataProviderMessage:
    out: CreateDataProviderMessage = {}  # type: ignore[typeddict-item]
    if "DataProviderName" in data:
        out["data_provider_name"] = data["DataProviderName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    else:
        raise DeserializationError("CreateDataProviderMessage.engine required")
    if "Virtual" in data:
        out["virtual"] = data["Virtual"]
    if "Settings" in data:
        import aws_sdk_database_migration_service.types.data_provider_settings

        out["settings"] = (
            aws_sdk_database_migration_service.types.data_provider_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    else:
        raise DeserializationError("CreateDataProviderMessage.settings required")
    if "Tags" in data:
        import aws_sdk_database_migration_service.types.tag_list

        out["tags"] = (
            aws_sdk_database_migration_service.types.tag_list.deserialize_aws_json_1_1(
                data["Tags"]
            )
        )
    return out
