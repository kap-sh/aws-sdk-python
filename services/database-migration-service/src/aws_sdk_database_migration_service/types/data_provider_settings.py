"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DataProviderSettings``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_database_migration_service.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.doc_db_data_provider_settings
    import aws_sdk_database_migration_service.types.ibm_db2_luw_data_provider_settings
    import aws_sdk_database_migration_service.types.ibm_db2z_os_data_provider_settings
    import aws_sdk_database_migration_service.types.maria_db_data_provider_settings
    import aws_sdk_database_migration_service.types.microsoft_sql_server_data_provider_settings
    import aws_sdk_database_migration_service.types.mongo_db_data_provider_settings
    import aws_sdk_database_migration_service.types.my_sql_data_provider_settings
    import aws_sdk_database_migration_service.types.oracle_data_provider_settings
    import aws_sdk_database_migration_service.types.postgre_sql_data_provider_settings
    import aws_sdk_database_migration_service.types.redshift_data_provider_settings
    import aws_sdk_database_migration_service.types.sybase_ase_data_provider_settings


class _DataProviderSettings_RedshiftSettings(TypedDict):
    RedshiftSettings: "aws_sdk_database_migration_service.types.redshift_data_provider_settings.RedshiftDataProviderSettings"


class _DataProviderSettings_PostgreSqlSettings(TypedDict):
    PostgreSqlSettings: "aws_sdk_database_migration_service.types.postgre_sql_data_provider_settings.PostgreSqlDataProviderSettings"


class _DataProviderSettings_MySqlSettings(TypedDict):
    MySqlSettings: "aws_sdk_database_migration_service.types.my_sql_data_provider_settings.MySqlDataProviderSettings"


class _DataProviderSettings_OracleSettings(TypedDict):
    OracleSettings: "aws_sdk_database_migration_service.types.oracle_data_provider_settings.OracleDataProviderSettings"


class _DataProviderSettings_SybaseAseSettings(TypedDict):
    SybaseAseSettings: "aws_sdk_database_migration_service.types.sybase_ase_data_provider_settings.SybaseAseDataProviderSettings"


class _DataProviderSettings_MicrosoftSqlServerSettings(TypedDict):
    MicrosoftSqlServerSettings: "aws_sdk_database_migration_service.types.microsoft_sql_server_data_provider_settings.MicrosoftSqlServerDataProviderSettings"


class _DataProviderSettings_DocDbSettings(TypedDict):
    DocDbSettings: "aws_sdk_database_migration_service.types.doc_db_data_provider_settings.DocDbDataProviderSettings"


class _DataProviderSettings_MariaDbSettings(TypedDict):
    MariaDbSettings: "aws_sdk_database_migration_service.types.maria_db_data_provider_settings.MariaDbDataProviderSettings"


class _DataProviderSettings_IbmDb2LuwSettings(TypedDict):
    IbmDb2LuwSettings: "aws_sdk_database_migration_service.types.ibm_db2_luw_data_provider_settings.IbmDb2LuwDataProviderSettings"


class _DataProviderSettings_IbmDb2zOsSettings(TypedDict):
    IbmDb2zOsSettings: "aws_sdk_database_migration_service.types.ibm_db2z_os_data_provider_settings.IbmDb2zOsDataProviderSettings"


class _DataProviderSettings_MongoDbSettings(TypedDict):
    MongoDbSettings: "aws_sdk_database_migration_service.types.mongo_db_data_provider_settings.MongoDbDataProviderSettings"


DataProviderSettings: TypeAlias = (
    _DataProviderSettings_RedshiftSettings
    | _DataProviderSettings_PostgreSqlSettings
    | _DataProviderSettings_MySqlSettings
    | _DataProviderSettings_OracleSettings
    | _DataProviderSettings_SybaseAseSettings
    | _DataProviderSettings_MicrosoftSqlServerSettings
    | _DataProviderSettings_DocDbSettings
    | _DataProviderSettings_MariaDbSettings
    | _DataProviderSettings_IbmDb2LuwSettings
    | _DataProviderSettings_IbmDb2zOsSettings
    | _DataProviderSettings_MongoDbSettings
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProviderSettings) -> dict:
    if "RedshiftSettings" in value:
        import aws_sdk_database_migration_service.types.redshift_data_provider_settings

        return {
            "RedshiftSettings": aws_sdk_database_migration_service.types.redshift_data_provider_settings.serialize_aws_json_1_1(
                value["RedshiftSettings"]
            )
        }
    elif "PostgreSqlSettings" in value:
        import aws_sdk_database_migration_service.types.postgre_sql_data_provider_settings

        return {
            "PostgreSqlSettings": aws_sdk_database_migration_service.types.postgre_sql_data_provider_settings.serialize_aws_json_1_1(
                value["PostgreSqlSettings"]
            )
        }
    elif "MySqlSettings" in value:
        import aws_sdk_database_migration_service.types.my_sql_data_provider_settings

        return {
            "MySqlSettings": aws_sdk_database_migration_service.types.my_sql_data_provider_settings.serialize_aws_json_1_1(
                value["MySqlSettings"]
            )
        }
    elif "OracleSettings" in value:
        import aws_sdk_database_migration_service.types.oracle_data_provider_settings

        return {
            "OracleSettings": aws_sdk_database_migration_service.types.oracle_data_provider_settings.serialize_aws_json_1_1(
                value["OracleSettings"]
            )
        }
    elif "SybaseAseSettings" in value:
        import aws_sdk_database_migration_service.types.sybase_ase_data_provider_settings

        return {
            "SybaseAseSettings": aws_sdk_database_migration_service.types.sybase_ase_data_provider_settings.serialize_aws_json_1_1(
                value["SybaseAseSettings"]
            )
        }
    elif "MicrosoftSqlServerSettings" in value:
        import aws_sdk_database_migration_service.types.microsoft_sql_server_data_provider_settings

        return {
            "MicrosoftSqlServerSettings": aws_sdk_database_migration_service.types.microsoft_sql_server_data_provider_settings.serialize_aws_json_1_1(
                value["MicrosoftSqlServerSettings"]
            )
        }
    elif "DocDbSettings" in value:
        import aws_sdk_database_migration_service.types.doc_db_data_provider_settings

        return {
            "DocDbSettings": aws_sdk_database_migration_service.types.doc_db_data_provider_settings.serialize_aws_json_1_1(
                value["DocDbSettings"]
            )
        }
    elif "MariaDbSettings" in value:
        import aws_sdk_database_migration_service.types.maria_db_data_provider_settings

        return {
            "MariaDbSettings": aws_sdk_database_migration_service.types.maria_db_data_provider_settings.serialize_aws_json_1_1(
                value["MariaDbSettings"]
            )
        }
    elif "IbmDb2LuwSettings" in value:
        import aws_sdk_database_migration_service.types.ibm_db2_luw_data_provider_settings

        return {
            "IbmDb2LuwSettings": aws_sdk_database_migration_service.types.ibm_db2_luw_data_provider_settings.serialize_aws_json_1_1(
                value["IbmDb2LuwSettings"]
            )
        }
    elif "IbmDb2zOsSettings" in value:
        import aws_sdk_database_migration_service.types.ibm_db2z_os_data_provider_settings

        return {
            "IbmDb2zOsSettings": aws_sdk_database_migration_service.types.ibm_db2z_os_data_provider_settings.serialize_aws_json_1_1(
                value["IbmDb2zOsSettings"]
            )
        }
    elif "MongoDbSettings" in value:
        import aws_sdk_database_migration_service.types.mongo_db_data_provider_settings

        return {
            "MongoDbSettings": aws_sdk_database_migration_service.types.mongo_db_data_provider_settings.serialize_aws_json_1_1(
                value["MongoDbSettings"]
            )
        }
    else:
        raise SerializationError("DataProviderSettings: no variant present")


def deserialize_aws_json_1_1(data: dict) -> DataProviderSettings:
    if "RedshiftSettings" in data:
        import aws_sdk_database_migration_service.types.redshift_data_provider_settings

        return {
            "RedshiftSettings": aws_sdk_database_migration_service.types.redshift_data_provider_settings.deserialize_aws_json_1_1(
                data["RedshiftSettings"]
            )
        }
    elif "PostgreSqlSettings" in data:
        import aws_sdk_database_migration_service.types.postgre_sql_data_provider_settings

        return {
            "PostgreSqlSettings": aws_sdk_database_migration_service.types.postgre_sql_data_provider_settings.deserialize_aws_json_1_1(
                data["PostgreSqlSettings"]
            )
        }
    elif "MySqlSettings" in data:
        import aws_sdk_database_migration_service.types.my_sql_data_provider_settings

        return {
            "MySqlSettings": aws_sdk_database_migration_service.types.my_sql_data_provider_settings.deserialize_aws_json_1_1(
                data["MySqlSettings"]
            )
        }
    elif "OracleSettings" in data:
        import aws_sdk_database_migration_service.types.oracle_data_provider_settings

        return {
            "OracleSettings": aws_sdk_database_migration_service.types.oracle_data_provider_settings.deserialize_aws_json_1_1(
                data["OracleSettings"]
            )
        }
    elif "SybaseAseSettings" in data:
        import aws_sdk_database_migration_service.types.sybase_ase_data_provider_settings

        return {
            "SybaseAseSettings": aws_sdk_database_migration_service.types.sybase_ase_data_provider_settings.deserialize_aws_json_1_1(
                data["SybaseAseSettings"]
            )
        }
    elif "MicrosoftSqlServerSettings" in data:
        import aws_sdk_database_migration_service.types.microsoft_sql_server_data_provider_settings

        return {
            "MicrosoftSqlServerSettings": aws_sdk_database_migration_service.types.microsoft_sql_server_data_provider_settings.deserialize_aws_json_1_1(
                data["MicrosoftSqlServerSettings"]
            )
        }
    elif "DocDbSettings" in data:
        import aws_sdk_database_migration_service.types.doc_db_data_provider_settings

        return {
            "DocDbSettings": aws_sdk_database_migration_service.types.doc_db_data_provider_settings.deserialize_aws_json_1_1(
                data["DocDbSettings"]
            )
        }
    elif "MariaDbSettings" in data:
        import aws_sdk_database_migration_service.types.maria_db_data_provider_settings

        return {
            "MariaDbSettings": aws_sdk_database_migration_service.types.maria_db_data_provider_settings.deserialize_aws_json_1_1(
                data["MariaDbSettings"]
            )
        }
    elif "IbmDb2LuwSettings" in data:
        import aws_sdk_database_migration_service.types.ibm_db2_luw_data_provider_settings

        return {
            "IbmDb2LuwSettings": aws_sdk_database_migration_service.types.ibm_db2_luw_data_provider_settings.deserialize_aws_json_1_1(
                data["IbmDb2LuwSettings"]
            )
        }
    elif "IbmDb2zOsSettings" in data:
        import aws_sdk_database_migration_service.types.ibm_db2z_os_data_provider_settings

        return {
            "IbmDb2zOsSettings": aws_sdk_database_migration_service.types.ibm_db2z_os_data_provider_settings.deserialize_aws_json_1_1(
                data["IbmDb2zOsSettings"]
            )
        }
    elif "MongoDbSettings" in data:
        import aws_sdk_database_migration_service.types.mongo_db_data_provider_settings

        return {
            "MongoDbSettings": aws_sdk_database_migration_service.types.mongo_db_data_provider_settings.deserialize_aws_json_1_1(
                data["MongoDbSettings"]
            )
        }
    else:
        raise DeserializationError("DataProviderSettings: no recognized variant key")
