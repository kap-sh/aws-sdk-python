"""Generated from Smithy shape ``com.amazonaws.firehose#RedshiftDestinationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.cluster_jdbcurl
    import aws_sdk_firehose.types.copy_command
    import aws_sdk_firehose.types.password
    import aws_sdk_firehose.types.processing_configuration
    import aws_sdk_firehose.types.redshift_retry_options
    import aws_sdk_firehose.types.redshift_s3_backup_mode
    import aws_sdk_firehose.types.role_arn
    import aws_sdk_firehose.types.s3_destination_update
    import aws_sdk_firehose.types.secrets_manager_configuration
    import aws_sdk_firehose.types.username


class RedshiftDestinationUpdate(TypedDict):
    role_arn: NotRequired["aws_sdk_firehose.types.role_arn.RoleARN"]
    r"""<p>The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    cluster_jdbcurl: NotRequired[
        "aws_sdk_firehose.types.cluster_jdbcurl.ClusterJDBCURL"
    ]
    """<p>The database connection string.</p>"""
    copy_command: NotRequired["aws_sdk_firehose.types.copy_command.CopyCommand"]
    """<p>The <code>COPY</code> command.</p>"""
    username: NotRequired["aws_sdk_firehose.types.username.Username"]
    """<p>The name of the user.</p>"""
    password: NotRequired["aws_sdk_firehose.types.password.Password"]
    """<p>The user password.</p>"""
    retry_options: NotRequired[
        "aws_sdk_firehose.types.redshift_retry_options.RedshiftRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).</p>"""
    s3_update: NotRequired[
        "aws_sdk_firehose.types.s3_destination_update.S3DestinationUpdate"
    ]
    """<p>The Amazon S3 destination.</p> <p>The compression formats <code>SNAPPY</code> or <code>ZIP</code> cannot be specified in <code>RedshiftDestinationUpdate.S3Update</code> because the Amazon Redshift <code>COPY</code> operation that reads from the S3 bucket doesn't support these compression formats.</p>"""
    processing_configuration: NotRequired[
        "aws_sdk_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    """<p>The data processing configuration.</p>"""
    s3_backup_mode: NotRequired[
        "aws_sdk_firehose.types.redshift_s3_backup_mode.RedshiftS3BackupMode"
    ]
    """<p>You can update a Firehose stream to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the Firehose stream to disable it. </p>"""
    s3_backup_update: NotRequired[
        "aws_sdk_firehose.types.s3_destination_update.S3DestinationUpdate"
    ]
    """<p>The Amazon S3 destination for backup.</p>"""
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>The Amazon CloudWatch logging options for your Firehose stream.</p>"""
    secrets_manager_configuration: NotRequired[
        "aws_sdk_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"
    ]
    """<p> The configuration that defines how you access secrets for Amazon Redshift. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDestinationUpdate) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "cluster_jdbcurl" in value:
        out["ClusterJDBCURL"] = value["cluster_jdbcurl"]
    if "copy_command" in value:
        import aws_sdk_firehose.types.copy_command

        out["CopyCommand"] = aws_sdk_firehose.types.copy_command.serialize_aws_json_1_1(
            value["copy_command"]
        )
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    if "retry_options" in value:
        import aws_sdk_firehose.types.redshift_retry_options

        out["RetryOptions"] = (
            aws_sdk_firehose.types.redshift_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_update" in value:
        import aws_sdk_firehose.types.s3_destination_update

        out["S3Update"] = (
            aws_sdk_firehose.types.s3_destination_update.serialize_aws_json_1_1(
                value["s3_update"]
            )
        )
    if "processing_configuration" in value:
        import aws_sdk_firehose.types.processing_configuration

        out["ProcessingConfiguration"] = (
            aws_sdk_firehose.types.processing_configuration.serialize_aws_json_1_1(
                value["processing_configuration"]
            )
        )
    if "s3_backup_mode" in value:
        import aws_sdk_firehose.types.redshift_s3_backup_mode

        out["S3BackupMode"] = (
            aws_sdk_firehose.types.redshift_s3_backup_mode.serialize_aws_json_1_1(
                value["s3_backup_mode"]
            )
        )
    if "s3_backup_update" in value:
        import aws_sdk_firehose.types.s3_destination_update

        out["S3BackupUpdate"] = (
            aws_sdk_firehose.types.s3_destination_update.serialize_aws_json_1_1(
                value["s3_backup_update"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "secrets_manager_configuration" in value:
        import aws_sdk_firehose.types.secrets_manager_configuration

        out["SecretsManagerConfiguration"] = (
            aws_sdk_firehose.types.secrets_manager_configuration.serialize_aws_json_1_1(
                value["secrets_manager_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDestinationUpdate:
    out: RedshiftDestinationUpdate = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "ClusterJDBCURL" in data:
        out["cluster_jdbcurl"] = data["ClusterJDBCURL"]
    if "CopyCommand" in data:
        import aws_sdk_firehose.types.copy_command

        out["copy_command"] = (
            aws_sdk_firehose.types.copy_command.deserialize_aws_json_1_1(
                data["CopyCommand"]
            )
        )
    if "Username" in data:
        out["username"] = data["Username"]
    if "Password" in data:
        out["password"] = data["Password"]
    if "RetryOptions" in data:
        import aws_sdk_firehose.types.redshift_retry_options

        out["retry_options"] = (
            aws_sdk_firehose.types.redshift_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "S3Update" in data:
        import aws_sdk_firehose.types.s3_destination_update

        out["s3_update"] = (
            aws_sdk_firehose.types.s3_destination_update.deserialize_aws_json_1_1(
                data["S3Update"]
            )
        )
    if "ProcessingConfiguration" in data:
        import aws_sdk_firehose.types.processing_configuration

        out["processing_configuration"] = (
            aws_sdk_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if "S3BackupMode" in data:
        import aws_sdk_firehose.types.redshift_s3_backup_mode

        out["s3_backup_mode"] = (
            aws_sdk_firehose.types.redshift_s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if "S3BackupUpdate" in data:
        import aws_sdk_firehose.types.s3_destination_update

        out["s3_backup_update"] = (
            aws_sdk_firehose.types.s3_destination_update.deserialize_aws_json_1_1(
                data["S3BackupUpdate"]
            )
        )
    if "CloudWatchLoggingOptions" in data:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if "SecretsManagerConfiguration" in data:
        import aws_sdk_firehose.types.secrets_manager_configuration

        out["secrets_manager_configuration"] = (
            aws_sdk_firehose.types.secrets_manager_configuration.deserialize_aws_json_1_1(
                data["SecretsManagerConfiguration"]
            )
        )
    return out
