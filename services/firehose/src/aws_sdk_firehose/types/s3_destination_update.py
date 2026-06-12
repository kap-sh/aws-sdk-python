"""Generated from Smithy shape ``com.amazonaws.firehose#S3DestinationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.bucket_arn
    import aws_sdk_firehose.types.buffering_hints
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.compression_format
    import aws_sdk_firehose.types.encryption_configuration
    import aws_sdk_firehose.types.error_output_prefix
    import aws_sdk_firehose.types.prefix
    import aws_sdk_firehose.types.role_arn


class S3DestinationUpdate(TypedDict):
    role_arn: NotRequired["aws_sdk_firehose.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    bucket_arn: NotRequired["aws_sdk_firehose.types.bucket_arn.BucketARN"]
    """<p>The ARN of the S3 bucket. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    prefix: NotRequired["aws_sdk_firehose.types.prefix.Prefix"]
    """<p>The \"YYYY/MM/DD/HH\" time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in <a href=\"https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html\">Custom Prefixes for Amazon S3 Objects</a>.</p>"""
    error_output_prefix: NotRequired[
        "aws_sdk_firehose.types.error_output_prefix.ErrorOutputPrefix"
    ]
    """<p>A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see <a href=\"https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html\">Custom Prefixes for Amazon S3 Objects</a>.</p>"""
    buffering_hints: NotRequired[
        "aws_sdk_firehose.types.buffering_hints.BufferingHints"
    ]
    """<p>The buffering option. If no value is specified, <code>BufferingHints</code> object default values are used.</p>"""
    compression_format: NotRequired[
        "aws_sdk_firehose.types.compression_format.CompressionFormat"
    ]
    """<p>The compression format. If no value is specified, the default is <code>UNCOMPRESSED</code>.</p> <p>The compression formats <code>SNAPPY</code> or <code>ZIP</code> cannot be specified for Amazon Redshift destinations because they are not supported by the Amazon Redshift <code>COPY</code> operation that reads from the S3 bucket.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_firehose.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration. If no value is specified, the default is no encryption.</p>"""
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>The CloudWatch logging options for your Firehose stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DestinationUpdate) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "bucket_arn" in value:
        out["BucketARN"] = value["bucket_arn"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "error_output_prefix" in value:
        out["ErrorOutputPrefix"] = value["error_output_prefix"]
    if "buffering_hints" in value:
        import aws_sdk_firehose.types.buffering_hints

        out["BufferingHints"] = (
            aws_sdk_firehose.types.buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "compression_format" in value:
        import aws_sdk_firehose.types.compression_format

        out["CompressionFormat"] = (
            aws_sdk_firehose.types.compression_format.serialize_aws_json_1_1(
                value["compression_format"]
            )
        )
    if "encryption_configuration" in value:
        import aws_sdk_firehose.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_firehose.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DestinationUpdate:
    out: S3DestinationUpdate = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "BucketARN" in data:
        out["bucket_arn"] = data["BucketARN"]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "ErrorOutputPrefix" in data:
        out["error_output_prefix"] = data["ErrorOutputPrefix"]
    if "BufferingHints" in data:
        import aws_sdk_firehose.types.buffering_hints

        out["buffering_hints"] = (
            aws_sdk_firehose.types.buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if "CompressionFormat" in data:
        import aws_sdk_firehose.types.compression_format

        out["compression_format"] = (
            aws_sdk_firehose.types.compression_format.deserialize_aws_json_1_1(
                data["CompressionFormat"]
            )
        )
    if "EncryptionConfiguration" in data:
        import aws_sdk_firehose.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_firehose.types.encryption_configuration.deserialize_aws_json_1_1(
                data["EncryptionConfiguration"]
            )
        )
    if "CloudWatchLoggingOptions" in data:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    return out
