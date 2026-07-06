"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DocDbDataProviderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.dms_ssl_mode_value
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class DocDbDataProviderSettings(TypedDict, closed=True):
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of the source DocumentDB server.</p>"""
    port: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port value for the DocumentDB data provider.</p>"""
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The database name on the DocumentDB data provider.</p>"""
    ssl_mode: NotRequired[
        "aws_sdk_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
    ]
    """<p>The SSL mode used to connect to the DocumentDB data provider. The default value is <code>none</code>.</p>"""
    certificate_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate used for SSL connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocDbDataProviderSettings) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> DocDbDataProviderSettings:
    out: DocDbDataProviderSettings = {}  # type: ignore[typeddict-item]
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
    return out
