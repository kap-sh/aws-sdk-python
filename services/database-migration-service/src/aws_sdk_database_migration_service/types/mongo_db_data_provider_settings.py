"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MongoDbDataProviderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.auth_mechanism_value
    import aws_sdk_database_migration_service.types.auth_type_value
    import aws_sdk_database_migration_service.types.dms_ssl_mode_value
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class MongoDbDataProviderSettings(TypedDict, closed=True):
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of the MongoDB server.</p>"""
    port: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port value for the MongoDB data provider.</p>"""
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The database name on the MongoDB data provider.</p>"""
    ssl_mode: NotRequired[
        "aws_sdk_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
    ]
    """<p>The SSL mode used to connect to the MongoDB data provider. The default value is <code>none</code>.</p>"""
    certificate_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate used for SSL connection.</p>"""
    auth_type: NotRequired[
        "aws_sdk_database_migration_service.types.auth_type_value.AuthTypeValue"
    ]
    """<p>The authentication type for the database connection. Valid values are PASSWORD or NO.</p>"""
    auth_source: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    r"""<p> The MongoDB database name. This setting isn't used when <code>AuthType</code> is set to <code>\"no\"</code>. </p> <p>The default is <code>\"admin\"</code>.</p>"""
    auth_mechanism: NotRequired[
        "aws_sdk_database_migration_service.types.auth_mechanism_value.AuthMechanismValue"
    ]
    """<p>The authentication method for connecting to the data provider. Valid values are DEFAULT, MONGODB_CR, or SCRAM_SHA_1.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MongoDbDataProviderSettings) -> dict:
    out: dict = {}
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "ssl_mode" in value:
        import aws_sdk_database_migration_service.types.dms_ssl_mode_value

        out["SslMode"] = (
            aws_sdk_database_migration_service.types.dms_ssl_mode_value.serialize_aws_json_1_1(
                value["ssl_mode"]
            )
        )
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "auth_type" in value:
        import aws_sdk_database_migration_service.types.auth_type_value

        out["AuthType"] = (
            aws_sdk_database_migration_service.types.auth_type_value.serialize_aws_json_1_1(
                value["auth_type"]
            )
        )
    if "auth_source" in value:
        out["AuthSource"] = value["auth_source"]
    if "auth_mechanism" in value:
        import aws_sdk_database_migration_service.types.auth_mechanism_value

        out["AuthMechanism"] = (
            aws_sdk_database_migration_service.types.auth_mechanism_value.serialize_aws_json_1_1(
                value["auth_mechanism"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MongoDbDataProviderSettings:
    out: MongoDbDataProviderSettings = {}  # type: ignore[typeddict-item]
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "SslMode" in data:
        import aws_sdk_database_migration_service.types.dms_ssl_mode_value

        out["ssl_mode"] = (
            aws_sdk_database_migration_service.types.dms_ssl_mode_value.deserialize_aws_json_1_1(
                data["SslMode"]
            )
        )
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "AuthType" in data:
        import aws_sdk_database_migration_service.types.auth_type_value

        out["auth_type"] = (
            aws_sdk_database_migration_service.types.auth_type_value.deserialize_aws_json_1_1(
                data["AuthType"]
            )
        )
    if "AuthSource" in data:
        out["auth_source"] = data["AuthSource"]
    if "AuthMechanism" in data:
        import aws_sdk_database_migration_service.types.auth_mechanism_value

        out["auth_mechanism"] = (
            aws_sdk_database_migration_service.types.auth_mechanism_value.deserialize_aws_json_1_1(
                data["AuthMechanism"]
            )
        )
    return out
