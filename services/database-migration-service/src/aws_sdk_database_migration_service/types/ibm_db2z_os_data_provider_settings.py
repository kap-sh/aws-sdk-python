"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#IbmDb2zOsDataProviderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.dms_ssl_mode_value
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class IbmDb2zOsDataProviderSettings(TypedDict, closed=True):
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of the DB2 for z/OS server.</p>"""
    port: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port value for the DB2 for z/OS data provider.</p>"""
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The database name on the DB2 for z/OS data provider.</p>"""
    ssl_mode: NotRequired[
        "aws_sdk_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
    ]
    """<p>The SSL mode used to connect to the DB2 for z/OS data provider. The default value is <code>none</code>. Valid Values: <code>none</code> and <code>verify-ca</code>.</p>"""
    certificate_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate used for SSL connection.</p>"""
    s3_path: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.</p>"""
    s3_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The ARN for the role the application uses to access its Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IbmDb2zOsDataProviderSettings) -> dict:
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
    if "s3_path" in value:
        out["S3Path"] = value["s3_path"]
    if "s3_access_role_arn" in value:
        out["S3AccessRoleArn"] = value["s3_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IbmDb2zOsDataProviderSettings:
    out: IbmDb2zOsDataProviderSettings = {}  # type: ignore[typeddict-item]
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
    if "S3Path" in data:
        out["s3_path"] = data["S3Path"]
    if "S3AccessRoleArn" in data:
        out["s3_access_role_arn"] = data["S3AccessRoleArn"]
    return out
