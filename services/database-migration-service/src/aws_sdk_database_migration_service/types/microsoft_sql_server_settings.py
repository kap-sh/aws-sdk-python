"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MicrosoftSQLServerSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.safeguard_policy
    import aws_sdk_database_migration_service.types.secret_string
    import aws_sdk_database_migration_service.types.sql_server_authentication_method
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.tlog_access_mode


class MicrosoftSQLServerSettings(TypedDict):
    port: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>Endpoint TCP port.</p>"""
    bcp_packet_size: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum size of the packets (in bytes) used to transfer data using BCP.</p>"""
    database_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Database name for the endpoint.</p>"""
    control_tables_file_group: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>Specifies a file group for the DMS internal tables. When the replication task starts, all the internal DMS control tables (awsdms_ apply_exception, awsdms_apply, awsdms_changes) are created for the specified file group.</p>"""
    password: NotRequired[
        "aws_sdk_database_migration_service.types.secret_string.SecretString"
    ]
    """<p>Endpoint connection password.</p>"""
    query_single_always_on_node: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Cleans and recreates table metadata information on the replication instance when a mismatch occurs. An example is a situation where running an alter DDL statement on a table might result in different information about the table cached in the replication instance.</p>"""
    read_backup_only: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When this attribute is set to <code>Y</code>, DMS only reads changes from transaction log backups and doesn't read from the active transaction log file during ongoing replication. Setting this parameter to <code>Y</code> enables you to control active transaction log file growth during full load and ongoing replication tasks. However, it can add some source latency to ongoing replication.</p>"""
    safeguard_policy: NotRequired[
        "aws_sdk_database_migration_service.types.safeguard_policy.SafeguardPolicy"
    ]
    """<p>Use this attribute to minimize the need to access the backup log and enable DMS to prevent truncation using one of the following two methods.</p> <p> <i>Start transactions in the database:</i> This is the default method. When this method is used, DMS prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started aren't truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method.</p> <p> <i>Exclusively use sp_repldone within a single task</i>: When this method is used, DMS reads the changes and then uses sp_repldone to mark the TLOG transactions as ready for truncation. Although this method doesn't involve any transactional activities, it can only be used when Microsoft Replication isn't running. Also, when using this method, only one DMS task can access the database at any given time. Therefore, if you need to run parallel DMS tasks against the same database, use the default method.</p>"""
    server_name: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    r"""<p>Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html\">DescribeDBInstances</a>, in the <code> <a href=\"https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html\">Endpoint</a>.Address</code> field.</p>"""
    username: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>Endpoint connection user name.</p>"""
    use_bcp_full_load: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Use this to attribute to transfer data for full-load operations using BCP. When the target table contains an identity column that does not exist in the source table, you must disable the use BCP for loading table option.</p>"""
    use_third_party_backup_device: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>When this attribute is set to <code>Y</code>, DMS processes third-party transaction log backups if they are created in native format.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    r"""<p>The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in <code>SecretsManagerSecret</code>. The role must allow the <code>iam:PassRole</code> action. <code>SecretsManagerSecret</code> has the value of the Amazon Web Services Secrets Manager secret that allows access to the SQL Server endpoint.</p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerSecretId</code>. Or you can specify clear-text values for <code>UserName</code>, <code>Password</code>, <code>ServerName</code>, and <code>Port</code>. You can't specify both. For more information on creating this <code>SecretsManagerSecret</code> and the <code>SecretsManagerAccessRoleArn</code> and <code>SecretsManagerSecretId</code> required to access it, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager\">Using secrets to access Database Migration Service resources</a> in the <i>Database Migration Service User Guide</i>.</p> </note>"""
    secrets_manager_secret_id: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The full ARN, partial ARN, or friendly name of the <code>SecretsManagerSecret</code> that contains the SQL Server endpoint connection details.</p>"""
    trim_space_in_char: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Use the <code>TrimSpaceInChar</code> source endpoint setting to right-trim data on CHAR and NCHAR data types during migration. Setting <code>TrimSpaceInChar</code> does not left-trim data. The default value is <code>true</code>.</p>"""
    tlog_access_mode: NotRequired[
        "aws_sdk_database_migration_service.types.tlog_access_mode.TlogAccessMode"
    ]
    """<p>Indicates the mode used to fetch CDC data.</p>"""
    force_lob_lookup: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>Forces LOB lookup on inline LOB.</p>"""
    authentication_method: NotRequired[
        "aws_sdk_database_migration_service.types.sql_server_authentication_method.SqlServerAuthenticationMethod"
    ]
    """<p>Specifies the authentication method to be used with Microsoft SQL Server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MicrosoftSQLServerSettings) -> dict:
    out: dict = {}
    if "port" in value:
        out["Port"] = value["port"]
    if "bcp_packet_size" in value:
        out["BcpPacketSize"] = value["bcp_packet_size"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "control_tables_file_group" in value:
        out["ControlTablesFileGroup"] = value["control_tables_file_group"]
    if "password" in value:
        out["Password"] = value["password"]
    if "query_single_always_on_node" in value:
        out["QuerySingleAlwaysOnNode"] = value["query_single_always_on_node"]
    if "read_backup_only" in value:
        out["ReadBackupOnly"] = value["read_backup_only"]
    if "safeguard_policy" in value:
        import aws_sdk_database_migration_service.types.safeguard_policy

        out["SafeguardPolicy"] = (
            aws_sdk_database_migration_service.types.safeguard_policy.serialize_aws_json_1_1(
                value["safeguard_policy"]
            )
        )
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "username" in value:
        out["Username"] = value["username"]
    if "use_bcp_full_load" in value:
        out["UseBcpFullLoad"] = value["use_bcp_full_load"]
    if "use_third_party_backup_device" in value:
        out["UseThirdPartyBackupDevice"] = value["use_third_party_backup_device"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    if "trim_space_in_char" in value:
        out["TrimSpaceInChar"] = value["trim_space_in_char"]
    if "tlog_access_mode" in value:
        import aws_sdk_database_migration_service.types.tlog_access_mode

        out["TlogAccessMode"] = (
            aws_sdk_database_migration_service.types.tlog_access_mode.serialize_aws_json_1_1(
                value["tlog_access_mode"]
            )
        )
    if "force_lob_lookup" in value:
        out["ForceLobLookup"] = value["force_lob_lookup"]
    if "authentication_method" in value:
        import aws_sdk_database_migration_service.types.sql_server_authentication_method

        out["AuthenticationMethod"] = (
            aws_sdk_database_migration_service.types.sql_server_authentication_method.serialize_aws_json_1_1(
                value["authentication_method"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MicrosoftSQLServerSettings:
    out: MicrosoftSQLServerSettings = {}  # type: ignore[typeddict-item]
    if "Port" in data:
        out["port"] = data["Port"]
    if "BcpPacketSize" in data:
        out["bcp_packet_size"] = data["BcpPacketSize"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "ControlTablesFileGroup" in data:
        out["control_tables_file_group"] = data["ControlTablesFileGroup"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "QuerySingleAlwaysOnNode" in data:
        out["query_single_always_on_node"] = data["QuerySingleAlwaysOnNode"]
    if "ReadBackupOnly" in data:
        out["read_backup_only"] = data["ReadBackupOnly"]
    if "SafeguardPolicy" in data:
        import aws_sdk_database_migration_service.types.safeguard_policy

        out["safeguard_policy"] = (
            aws_sdk_database_migration_service.types.safeguard_policy.deserialize_aws_json_1_1(
                data["SafeguardPolicy"]
            )
        )
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    if "Username" in data:
        out["username"] = data["Username"]
    if "UseBcpFullLoad" in data:
        out["use_bcp_full_load"] = data["UseBcpFullLoad"]
    if "UseThirdPartyBackupDevice" in data:
        out["use_third_party_backup_device"] = data["UseThirdPartyBackupDevice"]
    if "SecretsManagerAccessRoleArn" in data:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if "SecretsManagerSecretId" in data:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    if "TrimSpaceInChar" in data:
        out["trim_space_in_char"] = data["TrimSpaceInChar"]
    if "TlogAccessMode" in data:
        import aws_sdk_database_migration_service.types.tlog_access_mode

        out["tlog_access_mode"] = (
            aws_sdk_database_migration_service.types.tlog_access_mode.deserialize_aws_json_1_1(
                data["TlogAccessMode"]
            )
        )
    if "ForceLobLookup" in data:
        out["force_lob_lookup"] = data["ForceLobLookup"]
    if "AuthenticationMethod" in data:
        import aws_sdk_database_migration_service.types.sql_server_authentication_method

        out["authentication_method"] = (
            aws_sdk_database_migration_service.types.sql_server_authentication_method.deserialize_aws_json_1_1(
                data["AuthenticationMethod"]
            )
        )
    return out
