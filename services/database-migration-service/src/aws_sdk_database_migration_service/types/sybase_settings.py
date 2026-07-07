"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SybaseSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.secret_string
    import aws_sdk_database_migration_service.types.string


class SybaseSettings(TypedDict, closed=True):
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Database name for the endpoint.</p>"""
    password: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>Endpoint connection password.</p>"""
    port: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Endpoint TCP port. The default is 5000.</p>"""
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Fully qualified domain name of the endpoint.</p>"""
    username: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Endpoint connection user name.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    r"""<p>The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in <code>SecretsManagerSecret</code>. The role must allow the <code>iam:PassRole</code> action. <code>SecretsManagerSecret</code> has the value of the Amazon Web Services Secrets Manager secret that allows access to the SAP ASE endpoint.</p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerSecretId</code>. Or you can specify clear-text values for <code>UserName</code>, <code>Password</code>, <code>ServerName</code>, and <code>Port</code>. You can't specify both. For more information on creating this <code>SecretsManagerSecret</code> and the <code>SecretsManagerAccessRoleArn</code> and <code>SecretsManagerSecretId</code> required to access it, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager\">Using secrets to access Database Migration Service resources</a> in the <i>Database Migration Service User Guide</i>.</p> </note>"""
    secrets_manager_secret_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The full ARN, partial ARN, or friendly name of the <code>SecretsManagerSecret</code> that contains the SAP SAE endpoint connection details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SybaseSettings) -> dict:
    out: dict = {}
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "password" in value:
        out["Password"] = value["password"]
    if "port" in value:
        out["Port"] = value["port"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "username" in value:
        out["Username"] = value["username"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SybaseSettings:
    out: SybaseSettings = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    if "Username" in data:
        out["username"] = data["Username"]
    if "SecretsManagerAccessRoleArn" in data:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if "SecretsManagerSecretId" in data:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    return out
