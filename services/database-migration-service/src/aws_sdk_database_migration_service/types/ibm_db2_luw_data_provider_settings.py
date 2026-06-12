"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#IbmDb2LuwDataProviderSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.dms_ssl_mode_value
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class IbmDb2LuwDataProviderSettings(TypedDict):
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of the DB2 LUW server.</p>"""
    port: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port value for the DB2 LUW data provider.</p>"""
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The database name on the DB2 LUW data provider.</p>"""
    ssl_mode: NotRequired[
        "aws_sdk_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
    ]
    """<p>The SSL mode used to connect to the DB2 LUW data provider. The default value is <code>none</code>. Valid Values: <code>none</code> and <code>verify-ca</code>.</p>"""
    certificate_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate used for SSL connection.</p>"""
    encryption_algorithm: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The encryption algorithm used for securing the connection to the IBM DB2 LUW database server. You can provide an integer value corresponding to a specific encryption algorithm, or leave this parameter empty to use the default behavior. </p>"""
    security_mechanism: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The security mechanism used for authenticating the connection to the IBM DB2 LUW database server. You can provide an integer value corresponding to a specific security mechanism, or leave this parameter empty to use the default behavior. </p>"""
    s3_path: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.</p>"""
    s3_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The ARN for the role the application uses to access its Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IbmDb2LuwDataProviderSettings) -> dict:
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
    if "encryption_algorithm" in value:
        out["EncryptionAlgorithm"] = value["encryption_algorithm"]
    if "security_mechanism" in value:
        out["SecurityMechanism"] = value["security_mechanism"]
    if "s3_path" in value:
        out["S3Path"] = value["s3_path"]
    if "s3_access_role_arn" in value:
        out["S3AccessRoleArn"] = value["s3_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IbmDb2LuwDataProviderSettings:
    out: IbmDb2LuwDataProviderSettings = {}  # type: ignore[typeddict-item]
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
    if "EncryptionAlgorithm" in data:
        out["encryption_algorithm"] = data["EncryptionAlgorithm"]
    if "SecurityMechanism" in data:
        out["security_mechanism"] = data["SecurityMechanism"]
    if "S3Path" in data:
        out["s3_path"] = data["S3Path"]
    if "S3AccessRoleArn" in data:
        out["s3_access_role_arn"] = data["S3AccessRoleArn"]
    return out
