"""Generated from Smithy shape ``com.amazonaws.firehose#HttpEndpointDestinationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.http_endpoint_buffering_hints
    import aws_sdk_firehose.types.http_endpoint_configuration
    import aws_sdk_firehose.types.http_endpoint_request_configuration
    import aws_sdk_firehose.types.http_endpoint_retry_options
    import aws_sdk_firehose.types.http_endpoint_s3_backup_mode
    import aws_sdk_firehose.types.processing_configuration
    import aws_sdk_firehose.types.role_arn
    import aws_sdk_firehose.types.s3_destination_update
    import aws_sdk_firehose.types.secrets_manager_configuration


class HttpEndpointDestinationUpdate(TypedDict):
    endpoint_configuration: NotRequired[
        "aws_sdk_firehose.types.http_endpoint_configuration.HttpEndpointConfiguration"
    ]
    """<p>Describes the configuration of the HTTP endpoint destination.</p>"""
    buffering_hints: NotRequired[
        "aws_sdk_firehose.types.http_endpoint_buffering_hints.HttpEndpointBufferingHints"
    ]
    """<p>Describes buffering options that can be applied to the data before it is delivered to the HTTPS endpoint destination. Firehose teats these options as hints, and it might choose to use more optimal values. The <code>SizeInMBs</code> and <code>IntervalInSeconds</code> parameters are optional. However, if specify a value for one of them, you must also provide a value for the other. </p>"""
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    request_configuration: NotRequired[
        "aws_sdk_firehose.types.http_endpoint_request_configuration.HttpEndpointRequestConfiguration"
    ]
    """<p>The configuration of the request sent to the HTTP endpoint specified as the destination.</p>"""
    processing_configuration: NotRequired[
        "aws_sdk_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    role_arn: NotRequired["aws_sdk_firehose.types.role_arn.RoleARN"]
    """<p>Firehose uses this IAM role for all the permissions that the delivery stream needs.</p>"""
    retry_options: NotRequired[
        "aws_sdk_firehose.types.http_endpoint_retry_options.HttpEndpointRetryOptions"
    ]
    """<p>Describes the retry behavior in case Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.</p>"""
    s3_backup_mode: NotRequired[
        "aws_sdk_firehose.types.http_endpoint_s3_backup_mode.HttpEndpointS3BackupMode"
    ]
    """<p>Describes the S3 bucket backup options for the data that Kinesis Firehose delivers to the HTTP endpoint destination. You can back up all documents (<code>AllData</code>) or only the documents that Firehose could not deliver to the specified HTTP endpoint destination (<code>FailedDataOnly</code>).</p>"""
    s3_update: NotRequired[
        "aws_sdk_firehose.types.s3_destination_update.S3DestinationUpdate"
    ]
    secrets_manager_configuration: NotRequired[
        "aws_sdk_firehose.types.secrets_manager_configuration.SecretsManagerConfiguration"
    ]
    """<p> The configuration that defines how you access secrets for HTTP Endpoint destination. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HttpEndpointDestinationUpdate) -> dict:
    out: dict = {}
    if "endpoint_configuration" in value:
        import aws_sdk_firehose.types.http_endpoint_configuration

        out["EndpointConfiguration"] = (
            aws_sdk_firehose.types.http_endpoint_configuration.serialize_aws_json_1_1(
                value["endpoint_configuration"]
            )
        )
    if "buffering_hints" in value:
        import aws_sdk_firehose.types.http_endpoint_buffering_hints

        out["BufferingHints"] = (
            aws_sdk_firehose.types.http_endpoint_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "request_configuration" in value:
        import aws_sdk_firehose.types.http_endpoint_request_configuration

        out["RequestConfiguration"] = (
            aws_sdk_firehose.types.http_endpoint_request_configuration.serialize_aws_json_1_1(
                value["request_configuration"]
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
        import aws_sdk_firehose.types.http_endpoint_retry_options

        out["RetryOptions"] = (
            aws_sdk_firehose.types.http_endpoint_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import aws_sdk_firehose.types.http_endpoint_s3_backup_mode

        out["S3BackupMode"] = (
            aws_sdk_firehose.types.http_endpoint_s3_backup_mode.serialize_aws_json_1_1(
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
    return out


def deserialize_aws_json_1_1(data: dict) -> HttpEndpointDestinationUpdate:
    out: HttpEndpointDestinationUpdate = {}  # type: ignore[typeddict-item]
    if "EndpointConfiguration" in data:
        import aws_sdk_firehose.types.http_endpoint_configuration

        out["endpoint_configuration"] = (
            aws_sdk_firehose.types.http_endpoint_configuration.deserialize_aws_json_1_1(
                data["EndpointConfiguration"]
            )
        )
    if "BufferingHints" in data:
        import aws_sdk_firehose.types.http_endpoint_buffering_hints

        out["buffering_hints"] = (
            aws_sdk_firehose.types.http_endpoint_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if "CloudWatchLoggingOptions" in data:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if "RequestConfiguration" in data:
        import aws_sdk_firehose.types.http_endpoint_request_configuration

        out["request_configuration"] = (
            aws_sdk_firehose.types.http_endpoint_request_configuration.deserialize_aws_json_1_1(
                data["RequestConfiguration"]
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
        import aws_sdk_firehose.types.http_endpoint_retry_options

        out["retry_options"] = (
            aws_sdk_firehose.types.http_endpoint_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "S3BackupMode" in data:
        import aws_sdk_firehose.types.http_endpoint_s3_backup_mode

        out["s3_backup_mode"] = (
            aws_sdk_firehose.types.http_endpoint_s3_backup_mode.deserialize_aws_json_1_1(
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
    return out
