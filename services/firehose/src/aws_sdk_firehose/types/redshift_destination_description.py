"""Generated from Smithy shape ``com.amazonaws.firehose#RedshiftDestinationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.cluster_jdbcurl
    import aws_sdk_firehose.types.copy_command
    import aws_sdk_firehose.types.processing_configuration
    import aws_sdk_firehose.types.redshift_retry_options
    import aws_sdk_firehose.types.redshift_s3_backup_mode
    import aws_sdk_firehose.types.role_arn
    import aws_sdk_firehose.types.s3_destination_description
    import aws_sdk_firehose.types.secrets_manager_configuration
    import aws_sdk_firehose.types.username


class RedshiftDestinationDescription(TypedDict):
    role_arn: "aws_sdk_firehose.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    cluster_jdbcurl: "aws_sdk_firehose.types.cluster_jdbcurl.ClusterJDBCURL"
    """<p>The database connection string.</p>"""
    copy_command: "aws_sdk_firehose.types.copy_command.CopyCommand"
    """<p>The <code>COPY</code> command.</p>"""
    username: NotRequired["aws_sdk_firehose.types.username.Username"]
    """<p>The name of the user.</p>"""
    retry_options: NotRequired[
        "aws_sdk_firehose.types.redshift_retry_options.RedshiftRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).</p>"""
    s3_destination_description: (
        "aws_sdk_firehose.types.s3_destination_description.S3DestinationDescription"
    )
    """<p>The Amazon S3 destination.</p>"""
    processing_configuration: NotRequired[
        "aws_sdk_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    """<p>The data processing configuration.</p>"""
    s3_backup_mode: NotRequired[
        "aws_sdk_firehose.types.redshift_s3_backup_mode.RedshiftS3BackupMode"
    ]
    """<p>The Amazon S3 backup mode.</p>"""
    s3_backup_description: NotRequired[
        "aws_sdk_firehose.types.s3_destination_description.S3DestinationDescription"
    ]
    """<p>The configuration for backup in Amazon S3.</p>"""
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>The Amazon CloudWatch logging options for your Firehose stream.</p>"""
    secrets_manager_configuration: NotRequired[
        "aws_sdk_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"
    ]
    """<p> The configuration that defines how you access secrets for Amazon Redshift. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDestinationDescription) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    out["ClusterJDBCURL"] = value["cluster_jdbcurl"]
    import aws_sdk_firehose.types.copy_command

    out["CopyCommand"] = aws_sdk_firehose.types.copy_command.serialize_aws_json_1_1(
        value["copy_command"]
    )
    if "username" in value:
        out["Username"] = value["username"]
    if "retry_options" in value:
        import aws_sdk_firehose.types.redshift_retry_options

        out["RetryOptions"] = (
            aws_sdk_firehose.types.redshift_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    import aws_sdk_firehose.types.s3_destination_description

    out["S3DestinationDescription"] = (
        aws_sdk_firehose.types.s3_destination_description.serialize_aws_json_1_1(
            value["s3_destination_description"]
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
    if "s3_backup_description" in value:
        import aws_sdk_firehose.types.s3_destination_description

        out["S3BackupDescription"] = (
            aws_sdk_firehose.types.s3_destination_description.serialize_aws_json_1_1(
                value["s3_backup_description"]
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


def deserialize_aws_json_1_1(data: dict) -> RedshiftDestinationDescription:
    out: RedshiftDestinationDescription = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError("RedshiftDestinationDescription.role_arn required")
    if "ClusterJDBCURL" in data:
        out["cluster_jdbcurl"] = data["ClusterJDBCURL"]
    else:
        raise DeserializationError(
            "RedshiftDestinationDescription.cluster_jdbcurl required"
        )
    if "CopyCommand" in data:
        import aws_sdk_firehose.types.copy_command

        out["copy_command"] = (
            aws_sdk_firehose.types.copy_command.deserialize_aws_json_1_1(
                data["CopyCommand"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftDestinationDescription.copy_command required"
        )
    if "Username" in data:
        out["username"] = data["Username"]
    if "RetryOptions" in data:
        import aws_sdk_firehose.types.redshift_retry_options

        out["retry_options"] = (
            aws_sdk_firehose.types.redshift_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "S3DestinationDescription" in data:
        import aws_sdk_firehose.types.s3_destination_description

        out["s3_destination_description"] = (
            aws_sdk_firehose.types.s3_destination_description.deserialize_aws_json_1_1(
                data["S3DestinationDescription"]
            )
        )
    else:
        raise DeserializationError(
            "RedshiftDestinationDescription.s3_destination_description required"
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
    if "S3BackupDescription" in data:
        import aws_sdk_firehose.types.s3_destination_description

        out["s3_backup_description"] = (
            aws_sdk_firehose.types.s3_destination_description.deserialize_aws_json_1_1(
                data["S3BackupDescription"]
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
