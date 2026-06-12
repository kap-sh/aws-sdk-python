"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#IBMDb2Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.secret_string
    import aws_sdk_database_migration_service.types.string


class IBMDb2Settings(TypedDict):
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Database name for the endpoint.</p>"""
    password: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>Endpoint connection password.</p>"""
    port: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Endpoint TCP port. The default value is 50000.</p>"""
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Fully qualified domain name of the endpoint.</p>"""
    set_data_capture_changes: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Enables ongoing replication (CDC) as a BOOLEAN value. The default is true.</p>"""
    current_lsn: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.</p>"""
    max_k_bytes_per_read: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Maximum number of bytes per read, as a NUMBER value. The default is 64 KB.</p>"""
    username: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Endpoint connection user name.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in <code>SecretsManagerSecret</code>. The role must allow the <code>iam:PassRole</code> action. <code>SecretsManagerSecret</code> has the value of the Amazon Web Services Secrets Manager secret that allows access to the Db2 LUW endpoint. </p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerSecretId</code>. Or you can specify clear-text values for <code>UserName</code>, <code>Password</code>, <code>ServerName</code>, and <code>Port</code>. You can't specify both. For more information on creating this <code>SecretsManagerSecret</code> and the <code>SecretsManagerAccessRoleArn</code> and <code>SecretsManagerSecretId</code> required to access it, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager\">Using secrets to access Database Migration Service resources</a> in the <i>Database Migration Service User Guide</i>.</p> </note>"""
    secrets_manager_secret_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The full ARN, partial ARN, or friendly name of the <code>SecretsManagerSecret</code> that contains the Db2 LUW endpoint connection details.</p>"""
    load_timeout: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The amount of time (in milliseconds) before DMS times out operations performed by DMS on the Db2 target. The default value is 1200 (20 minutes).</p>"""
    write_buffer_size: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk on the DMS replication instance. The default value is 1024 (1 MB).</p>"""
    max_file_size: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Specifies the maximum size (in KB) of .csv files used to transfer data to Db2 LUW.</p>"""
    keep_csv_files: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If true, DMS saves any .csv files to the Db2 LUW target that were used to replicate data. DMS uses these files for analysis and troubleshooting.</p> <p>The default value is false. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IBMDb2Settings) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "port" in value:
        out["Port"] = value["port"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "set_data_capture_changes" in value:
        out["SetDataCaptureChanges"] = value["set_data_capture_changes"]
    if "current_lsn" in value:
        out["CurrentLsn"] = value["current_lsn"]
    if "max_k_bytes_per_read" in value:
        out["MaxKBytesPerRead"] = value["max_k_bytes_per_read"]
    if "username" in value:
        out["Username"] = value["username"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    if "load_timeout" in value:
        out["LoadTimeout"] = value["load_timeout"]
    if "write_buffer_size" in value:
        out["WriteBufferSize"] = value["write_buffer_size"]
    if "max_file_size" in value:
        out["MaxFileSize"] = value["max_file_size"]
    if "keep_csv_files" in value:
        out["KeepCsvFiles"] = value["keep_csv_files"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IBMDb2Settings:
    out: IBMDb2Settings = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    if "SetDataCaptureChanges" in data:
        out["set_data_capture_changes"] = data["SetDataCaptureChanges"]
    if "CurrentLsn" in data:
        out["current_lsn"] = data["CurrentLsn"]
    if "MaxKBytesPerRead" in data:
        out["max_k_bytes_per_read"] = data["MaxKBytesPerRead"]
    if "Username" in data:
        out["username"] = data["Username"]
    if "SecretsManagerAccessRoleArn" in data:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if "SecretsManagerSecretId" in data:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    if "LoadTimeout" in data:
        out["load_timeout"] = data["LoadTimeout"]
    if "WriteBufferSize" in data:
        out["write_buffer_size"] = data["WriteBufferSize"]
    if "MaxFileSize" in data:
        out["max_file_size"] = data["MaxFileSize"]
    if "KeepCsvFiles" in data:
        out["keep_csv_files"] = data["KeepCsvFiles"]
    return out
