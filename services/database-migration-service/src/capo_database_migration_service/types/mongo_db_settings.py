"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MongoDbSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.auth_mechanism_value
    import capo_database_migration_service.types.auth_type_value
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.nesting_level_value
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.string


class MongoDbSettings(TypedDict, closed=True):
    username: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The user name you use to access the MongoDB source endpoint. </p>"""
    password: NotRequired[
        "capo_database_migration_service.types.secret_string.SecretString"
    ]
    """<p> The password for the user account you use to access the MongoDB source endpoint. </p>"""
    server_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The name of the server on the MongoDB source endpoint. For MongoDB Atlas, provide the server name for any of the servers in the replication set.</p>"""
    port: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The port value for the MongoDB source endpoint. </p>"""
    database_name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p> The database name on the MongoDB source endpoint. </p>"""
    auth_type: NotRequired[
        "capo_database_migration_service.types.auth_type_value.AuthTypeValue"
    ]
    r"""<p> The authentication type you use to access the MongoDB source endpoint.</p> <p>When when set to <code>\"no\"</code>, user name and password parameters are not used and can be empty. </p>"""
    auth_mechanism: NotRequired[
        "capo_database_migration_service.types.auth_mechanism_value.AuthMechanismValue"
    ]
    r"""<p> The authentication mechanism you use to access the MongoDB source endpoint.</p> <p>For the default value, in MongoDB version 2.x, <code>\"default\"</code> is <code>\"mongodb_cr\"</code>. For MongoDB version 3.x or later, <code>\"default\"</code> is <code>\"scram_sha_1\"</code>. This setting isn't used when <code>AuthType</code> is set to <code>\"no\"</code>.</p>"""
    nesting_level: NotRequired[
        "capo_database_migration_service.types.nesting_level_value.NestingLevelValue"
    ]
    r"""<p> Specifies either document or table mode. </p> <p>Default value is <code>\"none\"</code>. Specify <code>\"none\"</code> to use document mode. Specify <code>\"one\"</code> to use table mode.</p>"""
    extract_doc_id: NotRequired["capo_database_migration_service.types.string.String"]
    r"""<p> Specifies the document ID. Use this setting when <code>NestingLevel</code> is set to <code>\"none\"</code>. </p> <p>Default value is <code>\"false\"</code>. </p>"""
    docs_to_investigate: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    r"""<p> Indicates the number of documents to preview to determine the document organization. Use this setting when <code>NestingLevel</code> is set to <code>\"one\"</code>. </p> <p>Must be a positive value greater than <code>0</code>. Default value is <code>1000</code>.</p>"""
    auth_source: NotRequired["capo_database_migration_service.types.string.String"]
    r"""<p> The MongoDB database name. This setting isn't used when <code>AuthType</code> is set to <code>\"no\"</code>. </p> <p>The default is <code>\"admin\"</code>.</p>"""
    kms_key_id: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The KMS key identifier that is used to encrypt the content on the replication instance. If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key. KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>"""
    secrets_manager_access_role_arn: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    r"""<p>The full Amazon Resource Name (ARN) of the IAM role that specifies DMS as the trusted entity and grants the required permissions to access the value in <code>SecretsManagerSecret</code>. The role must allow the <code>iam:PassRole</code> action. <code>SecretsManagerSecret</code> has the value of the Amazon Web Services Secrets Manager secret that allows access to the MongoDB endpoint.</p> <note> <p>You can specify one of two sets of values for these permissions. You can specify the values for this setting and <code>SecretsManagerSecretId</code>. Or you can specify clear-text values for <code>UserName</code>, <code>Password</code>, <code>ServerName</code>, and <code>Port</code>. You can't specify both. For more information on creating this <code>SecretsManagerSecret</code> and the <code>SecretsManagerAccessRoleArn</code> and <code>SecretsManagerSecretId</code> required to access it, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager\">Using secrets to access Database Migration Service resources</a> in the <i>Database Migration Service User Guide</i>.</p> </note>"""
    secrets_manager_secret_id: NotRequired[
        "capo_database_migration_service.types.string.String"
    ]
    """<p>The full ARN, partial ARN, or friendly name of the <code>SecretsManagerSecret</code> that contains the MongoDB endpoint connection details.</p>"""
    use_update_look_up: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, DMS retrieves the entire document from the MongoDB source during migration. This may cause a migration failure if the server response exceeds bandwidth limits. To fetch only updates and deletes during migration, set this parameter to <code>false</code>.</p>"""
    replicate_shard_collections: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, DMS replicates data to shard collections. DMS only uses this setting if the target endpoint is a DocumentDB elastic cluster.</p> <p>When this setting is <code>true</code>, note the following:</p> <ul> <li> <p>You must set <code>TargetTablePrepMode</code> to <code>nothing</code>.</p> </li> <li> <p>DMS automatically sets <code>useUpdateLookup</code> to <code>false</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MongoDbSettings) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "port" in value:
        out["Port"] = value["port"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "auth_type" in value:
        import capo_database_migration_service.types.auth_type_value

        out["AuthType"] = (
            capo_database_migration_service.types.auth_type_value.serialize_aws_json_1_1(
                value["auth_type"]
            )
        )
    if "auth_mechanism" in value:
        import capo_database_migration_service.types.auth_mechanism_value

        out["AuthMechanism"] = (
            capo_database_migration_service.types.auth_mechanism_value.serialize_aws_json_1_1(
                value["auth_mechanism"]
            )
        )
    if "nesting_level" in value:
        import capo_database_migration_service.types.nesting_level_value

        out["NestingLevel"] = (
            capo_database_migration_service.types.nesting_level_value.serialize_aws_json_1_1(
                value["nesting_level"]
            )
        )
    if "extract_doc_id" in value:
        out["ExtractDocId"] = value["extract_doc_id"]
    if "docs_to_investigate" in value:
        out["DocsToInvestigate"] = value["docs_to_investigate"]
    if "auth_source" in value:
        out["AuthSource"] = value["auth_source"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "secrets_manager_access_role_arn" in value:
        out["SecretsManagerAccessRoleArn"] = value["secrets_manager_access_role_arn"]
    if "secrets_manager_secret_id" in value:
        out["SecretsManagerSecretId"] = value["secrets_manager_secret_id"]
    if "use_update_look_up" in value:
        out["UseUpdateLookUp"] = value["use_update_look_up"]
    if "replicate_shard_collections" in value:
        out["ReplicateShardCollections"] = value["replicate_shard_collections"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MongoDbSettings:
    out: MongoDbSettings = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "AuthType" in data:
        import capo_database_migration_service.types.auth_type_value

        out["auth_type"] = (
            capo_database_migration_service.types.auth_type_value.deserialize_aws_json_1_1(
                data["AuthType"]
            )
        )
    if "AuthMechanism" in data:
        import capo_database_migration_service.types.auth_mechanism_value

        out["auth_mechanism"] = (
            capo_database_migration_service.types.auth_mechanism_value.deserialize_aws_json_1_1(
                data["AuthMechanism"]
            )
        )
    if "NestingLevel" in data:
        import capo_database_migration_service.types.nesting_level_value

        out["nesting_level"] = (
            capo_database_migration_service.types.nesting_level_value.deserialize_aws_json_1_1(
                data["NestingLevel"]
            )
        )
    if "ExtractDocId" in data:
        out["extract_doc_id"] = data["ExtractDocId"]
    if "DocsToInvestigate" in data:
        out["docs_to_investigate"] = data["DocsToInvestigate"]
    if "AuthSource" in data:
        out["auth_source"] = data["AuthSource"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "SecretsManagerAccessRoleArn" in data:
        out["secrets_manager_access_role_arn"] = data["SecretsManagerAccessRoleArn"]
    if "SecretsManagerSecretId" in data:
        out["secrets_manager_secret_id"] = data["SecretsManagerSecretId"]
    if "UseUpdateLookUp" in data:
        out["use_update_look_up"] = data["UseUpdateLookUp"]
    if "ReplicateShardCollections" in data:
        out["replicate_shard_collections"] = data["ReplicateShardCollections"]
    return out
