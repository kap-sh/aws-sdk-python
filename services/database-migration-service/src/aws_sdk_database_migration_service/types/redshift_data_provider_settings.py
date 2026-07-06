"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RedshiftDataProviderSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class RedshiftDataProviderSettings(TypedDict, closed=True):
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The name of the Amazon Redshift server.</p>"""
    port: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The port value for the Amazon Redshift data provider.</p>"""
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The database name on the Amazon Redshift data provider.</p>"""
    s3_path: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The path for the Amazon S3 bucket that the application uses for accessing the user-defined schema.</p>"""
    s3_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The ARN for the role the application uses to access its Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDataProviderSettings) -> dict:
    out: dict = {}
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "s3_path" in value:
        out["S3Path"] = value["s3_path"]
    if "s3_access_role_arn" in value:
        out["S3AccessRoleArn"] = value["s3_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDataProviderSettings:
    out: RedshiftDataProviderSettings = {}  # type: ignore[typeddict-item]
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "S3Path" in data:
        out["s3_path"] = data["S3Path"]
    if "S3AccessRoleArn" in data:
        out["s3_access_role_arn"] = data["S3AccessRoleArn"]
    return out
