"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ModifyDataProviderMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.data_provider_settings
    import aws_sdk_database_migration_service.types.string


class ModifyDataProviderMessage(TypedDict):
    data_provider_identifier: "aws_sdk_database_migration_service.types.string.String"
    """<p>The identifier of the data provider. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>"""
    data_provider_name: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The name of the data provider.</p>"""
    description: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A user-friendly description of the data provider.</p>"""
    engine: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    r"""<p>The type of database engine for the data provider. Valid values include <code>\"aurora\"</code>, <code>\"aurora-postgresql\"</code>, <code>\"mysql\"</code>, <code>\"oracle\"</code>, <code>\"postgres\"</code>, <code>\"sqlserver\"</code>, <code>redshift</code>, <code>mariadb</code>, <code>mongodb</code>, <code>db2</code>, <code>db2-zos</code>, <code>docdb</code>, and <code>sybase</code>. A value of <code>\"aurora\"</code> represents Amazon Aurora MySQL-Compatible Edition.</p>"""
    virtual: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates whether the data provider is virtual.</p>"""
    exact_settings: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this attribute is Y, the current call to <code>ModifyDataProvider</code> replaces all existing data provider settings with the exact settings that you specify in this call. If this attribute is N, the current call to <code>ModifyDataProvider</code> does two things: </p> <ul> <li> <p>It replaces any data provider settings that already exist with new values, for settings with the same names.</p> </li> <li> <p>It creates new data provider settings that you specify in the call, for settings with different names. </p> </li> </ul>"""
    settings: NotRequired[
        "aws_sdk_database_migration_service.types.data_provider_settings.DataProviderSettings"
    ]
    """<p>The settings in JSON format for a data provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyDataProviderMessage) -> dict:
    out: dict = {}
    out["DataProviderIdentifier"] = value["data_provider_identifier"]
    if "data_provider_name" in value:
        out["DataProviderName"] = value["data_provider_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "virtual" in value:
        out["Virtual"] = value["virtual"]
    if "exact_settings" in value:
        out["ExactSettings"] = value["exact_settings"]
    if "settings" in value:
        import aws_sdk_database_migration_service.types.data_provider_settings

        out["Settings"] = (
            aws_sdk_database_migration_service.types.data_provider_settings.serialize_aws_json_1_1(
                value["settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyDataProviderMessage:
    out: ModifyDataProviderMessage = {}  # type: ignore[typeddict-item]
    if "DataProviderIdentifier" in data:
        out["data_provider_identifier"] = data["DataProviderIdentifier"]
    else:
        raise DeserializationError(
            "ModifyDataProviderMessage.data_provider_identifier required"
        )
    if "DataProviderName" in data:
        out["data_provider_name"] = data["DataProviderName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "Virtual" in data:
        out["virtual"] = data["Virtual"]
    if "ExactSettings" in data:
        out["exact_settings"] = data["ExactSettings"]
    if "Settings" in data:
        import aws_sdk_database_migration_service.types.data_provider_settings

        out["settings"] = (
            aws_sdk_database_migration_service.types.data_provider_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    return out
