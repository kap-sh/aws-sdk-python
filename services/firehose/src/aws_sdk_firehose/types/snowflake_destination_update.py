"""Generated from Smithy shape ``com.amazonaws.firehose#SnowflakeDestinationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.processing_configuration
    import aws_sdk_firehose.types.role_arn
    import aws_sdk_firehose.types.s3_destination_update
    import aws_sdk_firehose.types.secrets_manager_configuration
    import aws_sdk_firehose.types.snowflake_account_url
    import aws_sdk_firehose.types.snowflake_buffering_hints
    import aws_sdk_firehose.types.snowflake_content_column_name
    import aws_sdk_firehose.types.snowflake_data_loading_option
    import aws_sdk_firehose.types.snowflake_database
    import aws_sdk_firehose.types.snowflake_key_passphrase
    import aws_sdk_firehose.types.snowflake_meta_data_column_name
    import aws_sdk_firehose.types.snowflake_private_key
    import aws_sdk_firehose.types.snowflake_retry_options
    import aws_sdk_firehose.types.snowflake_role_configuration
    import aws_sdk_firehose.types.snowflake_s3_backup_mode
    import aws_sdk_firehose.types.snowflake_schema
    import aws_sdk_firehose.types.snowflake_table
    import aws_sdk_firehose.types.snowflake_user


class SnowflakeDestinationUpdate(TypedDict):
    account_url: NotRequired[
        "aws_sdk_firehose.types.snowflake_account_url.SnowflakeAccountUrl"
    ]
    """<p>URL for accessing your Snowflake account. This URL must include your <a href=\"https://docs.snowflake.com/en/user-guide/admin-account-identifier\">account identifier</a>. Note that the protocol (https://) and port number are optional.</p>"""
    private_key: NotRequired[
        "aws_sdk_firehose.types.snowflake_private_key.SnowflakePrivateKey"
    ]
    """<p>The private key used to encrypt your Snowflake client. For information, see <a href=\"https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation\">Using Key Pair Authentication & Key Rotation</a>.</p>"""
    key_passphrase: NotRequired[
        "aws_sdk_firehose.types.snowflake_key_passphrase.SnowflakeKeyPassphrase"
    ]
    """<p>Passphrase to decrypt the private key when the key is encrypted. For information, see <a href=\"https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation\">Using Key Pair Authentication & Key Rotation</a>.</p>"""
    user: NotRequired["aws_sdk_firehose.types.snowflake_user.SnowflakeUser"]
    """<p>User login name for the Snowflake account.</p>"""
    database: NotRequired["aws_sdk_firehose.types.snowflake_database.SnowflakeDatabase"]
    """<p>All data in Snowflake is maintained in databases.</p>"""
    schema: NotRequired["aws_sdk_firehose.types.snowflake_schema.SnowflakeSchema"]
    """<p>Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views</p>"""
    table: NotRequired["aws_sdk_firehose.types.snowflake_table.SnowflakeTable"]
    """<p>All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.</p>"""
    snowflake_role_configuration: NotRequired[
        "aws_sdk_firehose.types.snowflake_role_configuration.SnowflakeRoleConfiguration"
    ]
    """<p>Optionally configure a Snowflake role. Otherwise the default user role will be used.</p>"""
    data_loading_option: NotRequired[
        "aws_sdk_firehose.types.snowflake_data_loading_option.SnowflakeDataLoadingOption"
    ]
    """<p> JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.</p>"""
    meta_data_column_name: NotRequired[
        "aws_sdk_firehose.types.snowflake_meta_data_column_name.SnowflakeMetaDataColumnName"
    ]
    """<p>The name of the record metadata column</p>"""
    content_column_name: NotRequired[
        "aws_sdk_firehose.types.snowflake_content_column_name.SnowflakeContentColumnName"
    ]
    """<p>The name of the content metadata column</p>"""
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    processing_configuration: NotRequired[
        "aws_sdk_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    role_arn: NotRequired["aws_sdk_firehose.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the Snowflake role</p>"""
    retry_options: NotRequired[
        "aws_sdk_firehose.types.snowflake_retry_options.SnowflakeRetryOptions"
    ]
    """<p>Specify how long Firehose retries sending data to the New Relic HTTP endpoint. After sending data, Firehose first waits for an acknowledgment from the HTTP endpoint. If an error occurs or the acknowledgment doesn’t arrive within the acknowledgment timeout period, Firehose starts the retry duration counter. It keeps retrying until the retry duration expires. After that, Firehose considers it a data delivery failure and backs up the data to your Amazon S3 bucket. Every time that Firehose sends data to the HTTP endpoint (either the initial attempt or a retry), it restarts the acknowledgement timeout counter and waits for an acknowledgement from the HTTP endpoint. Even if the retry duration expires, Firehose still waits for the acknowledgment until it receives it or the acknowledgement timeout period is reached. If the acknowledgment times out, Firehose determines whether there's time left in the retry counter. If there is time left, it retries again and repeats the logic until it receives an acknowledgment or determines that the retry time has expired. If you don't want Firehose to retry sending data, set this value to 0.</p>"""
    s3_backup_mode: NotRequired[
        "aws_sdk_firehose.types.snowflake_s3_backup_mode.SnowflakeS3BackupMode"
    ]
    """<p>Choose an S3 backup mode. Once you set the mode as <code>AllData</code>, you can not change it to <code>FailedDataOnly</code>.</p>"""
    s3_update: NotRequired[
        "aws_sdk_firehose.types.s3_destination_update.S3DestinationUpdate"
    ]
    secrets_manager_configuration: NotRequired[
        "aws_sdk_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"
    ]
    """<p> Describes the Secrets Manager configuration in Snowflake. </p>"""
    buffering_hints: NotRequired[
        "aws_sdk_firehose.types.snowflake_buffering_hints.SnowflakeBufferingHints"
    ]
    """<p> Describes the buffering to perform before delivering data to the Snowflake destination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnowflakeDestinationUpdate) -> dict:
    out: dict = {}
    if "account_url" in value:
        out["AccountUrl"] = value["account_url"]
    if "private_key" in value:
        out["PrivateKey"] = value["private_key"]
    if "key_passphrase" in value:
        out["KeyPassphrase"] = value["key_passphrase"]
    if "user" in value:
        out["User"] = value["user"]
    if "database" in value:
        out["Database"] = value["database"]
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "table" in value:
        out["Table"] = value["table"]
    if "snowflake_role_configuration" in value:
        import aws_sdk_firehose.types.snowflake_role_configuration

        out["SnowflakeRoleConfiguration"] = (
            aws_sdk_firehose.types.snowflake_role_configuration.serialize_aws_json_1_1(
                value["snowflake_role_configuration"]
            )
        )
    if "data_loading_option" in value:
        import aws_sdk_firehose.types.snowflake_data_loading_option

        out["DataLoadingOption"] = (
            aws_sdk_firehose.types.snowflake_data_loading_option.serialize_aws_json_1_1(
                value["data_loading_option"]
            )
        )
    if "meta_data_column_name" in value:
        out["MetaDataColumnName"] = value["meta_data_column_name"]
    if "content_column_name" in value:
        out["ContentColumnName"] = value["content_column_name"]
    if "cloud_watch_logging_options" in value:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "processing_configuration" in value:
        import aws_sdk_firehose.types.processing_configuration

        out["ProcessingConfiguration"] = (
            aws_sdk_firehose.types.processing_configuration.serialize_aws_json_1_1(
                value["processing_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "retry_options" in value:
        import aws_sdk_firehose.types.snowflake_retry_options

        out["RetryOptions"] = (
            aws_sdk_firehose.types.snowflake_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import aws_sdk_firehose.types.snowflake_s3_backup_mode

        out["S3BackupMode"] = (
            aws_sdk_firehose.types.snowflake_s3_backup_mode.serialize_aws_json_1_1(
                value["s3_backup_mode"]
            )
        )
    if "s3_update" in value:
        import aws_sdk_firehose.types.s3_destination_update

        out["S3Update"] = (
            aws_sdk_firehose.types.s3_destination_update.serialize_aws_json_1_1(
                value["s3_update"]
            )
        )
    if "secrets_manager_configuration" in value:
        import aws_sdk_firehose.types.secrets_manager_configuration

        out["SecretsManagerConfiguration"] = (
            aws_sdk_firehose.types.secrets_manager_configuration.serialize_aws_json_1_1(
                value["secrets_manager_configuration"]
            )
        )
    if "buffering_hints" in value:
        import aws_sdk_firehose.types.snowflake_buffering_hints

        out["BufferingHints"] = (
            aws_sdk_firehose.types.snowflake_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnowflakeDestinationUpdate:
    out: SnowflakeDestinationUpdate = {}  # type: ignore[typeddict-item]
    if "AccountUrl" in data:
        out["account_url"] = data["AccountUrl"]
    if "PrivateKey" in data:
        out["private_key"] = data["PrivateKey"]
    if "KeyPassphrase" in data:
        out["key_passphrase"] = data["KeyPassphrase"]
    if "User" in data:
        out["user"] = data["User"]
    if "Database" in data:
        out["database"] = data["Database"]
    if "Schema" in data:
        out["schema"] = data["Schema"]
    if "Table" in data:
        out["table"] = data["Table"]
    if "SnowflakeRoleConfiguration" in data:
        import aws_sdk_firehose.types.snowflake_role_configuration

        out["snowflake_role_configuration"] = (
            aws_sdk_firehose.types.snowflake_role_configuration.deserialize_aws_json_1_1(
                data["SnowflakeRoleConfiguration"]
            )
        )
    if "DataLoadingOption" in data:
        import aws_sdk_firehose.types.snowflake_data_loading_option

        out["data_loading_option"] = (
            aws_sdk_firehose.types.snowflake_data_loading_option.deserialize_aws_json_1_1(
                data["DataLoadingOption"]
            )
        )
    if "MetaDataColumnName" in data:
        out["meta_data_column_name"] = data["MetaDataColumnName"]
    if "ContentColumnName" in data:
        out["content_column_name"] = data["ContentColumnName"]
    if "CloudWatchLoggingOptions" in data:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if "ProcessingConfiguration" in data:
        import aws_sdk_firehose.types.processing_configuration

        out["processing_configuration"] = (
            aws_sdk_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "RetryOptions" in data:
        import aws_sdk_firehose.types.snowflake_retry_options

        out["retry_options"] = (
            aws_sdk_firehose.types.snowflake_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "S3BackupMode" in data:
        import aws_sdk_firehose.types.snowflake_s3_backup_mode

        out["s3_backup_mode"] = (
            aws_sdk_firehose.types.snowflake_s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if "S3Update" in data:
        import aws_sdk_firehose.types.s3_destination_update

        out["s3_update"] = (
            aws_sdk_firehose.types.s3_destination_update.deserialize_aws_json_1_1(
                data["S3Update"]
            )
        )
    if "SecretsManagerConfiguration" in data:
        import aws_sdk_firehose.types.secrets_manager_configuration

        out["secrets_manager_configuration"] = (
            aws_sdk_firehose.types.secrets_manager_configuration.deserialize_aws_json_1_1(
                data["SecretsManagerConfiguration"]
            )
        )
    if "BufferingHints" in data:
        import aws_sdk_firehose.types.snowflake_buffering_hints

        out["buffering_hints"] = (
            aws_sdk_firehose.types.snowflake_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    return out
