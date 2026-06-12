"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonOpenSearchServerlessDestinationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.amazon_open_search_serverless_buffering_hints
    import aws_sdk_firehose.types.amazon_open_search_serverless_collection_endpoint
    import aws_sdk_firehose.types.amazon_open_search_serverless_index_name
    import aws_sdk_firehose.types.amazon_open_search_serverless_retry_options
    import aws_sdk_firehose.types.amazon_open_search_serverless_s3_backup_mode
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.processing_configuration
    import aws_sdk_firehose.types.role_arn
    import aws_sdk_firehose.types.s3_destination_description
    import aws_sdk_firehose.types.vpc_configuration_description


class AmazonOpenSearchServerlessDestinationDescription(TypedDict):
    role_arn: NotRequired["aws_sdk_firehose.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services credentials.</p>"""
    collection_endpoint: NotRequired[
        "aws_sdk_firehose.types.amazon_open_search_serverless_collection_endpoint.AmazonOpenSearchServerlessCollectionEndpoint"
    ]
    """<p>The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.</p>"""
    index_name: NotRequired[
        "aws_sdk_firehose.types.amazon_open_search_serverless_index_name.AmazonOpenSearchServerlessIndexName"
    ]
    """<p>The Serverless offering for Amazon OpenSearch Service index name.</p>"""
    buffering_hints: NotRequired[
        "aws_sdk_firehose.types.amazon_open_search_serverless_buffering_hints.AmazonOpenSearchServerlessBufferingHints"
    ]
    """<p>The buffering options.</p>"""
    retry_options: NotRequired[
        "aws_sdk_firehose.types.amazon_open_search_serverless_retry_options.AmazonOpenSearchServerlessRetryOptions"
    ]
    """<p>The Serverless offering for Amazon OpenSearch Service retry options.</p>"""
    s3_backup_mode: NotRequired[
        "aws_sdk_firehose.types.amazon_open_search_serverless_s3_backup_mode.AmazonOpenSearchServerlessS3BackupMode"
    ]
    """<p>The Amazon S3 backup mode.</p>"""
    s3_destination_description: NotRequired[
        "aws_sdk_firehose.types.s3_destination_description.S3DestinationDescription"
    ]
    processing_configuration: NotRequired[
        "aws_sdk_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    vpc_configuration_description: NotRequired[
        "aws_sdk_firehose.types.vpc_configuration_description.VpcConfigurationDescription"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AmazonOpenSearchServerlessDestinationDescription,
) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "collection_endpoint" in value:
        out["CollectionEndpoint"] = value["collection_endpoint"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "buffering_hints" in value:
        import aws_sdk_firehose.types.amazon_open_search_serverless_buffering_hints

        out["BufferingHints"] = (
            aws_sdk_firehose.types.amazon_open_search_serverless_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "retry_options" in value:
        import aws_sdk_firehose.types.amazon_open_search_serverless_retry_options

        out["RetryOptions"] = (
            aws_sdk_firehose.types.amazon_open_search_serverless_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import aws_sdk_firehose.types.amazon_open_search_serverless_s3_backup_mode

        out["S3BackupMode"] = (
            aws_sdk_firehose.types.amazon_open_search_serverless_s3_backup_mode.serialize_aws_json_1_1(
                value["s3_backup_mode"]
            )
        )
    if "s3_destination_description" in value:
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
    if "cloud_watch_logging_options" in value:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "vpc_configuration_description" in value:
        import aws_sdk_firehose.types.vpc_configuration_description

        out["VpcConfigurationDescription"] = (
            aws_sdk_firehose.types.vpc_configuration_description.serialize_aws_json_1_1(
                value["vpc_configuration_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AmazonOpenSearchServerlessDestinationDescription:
    out: AmazonOpenSearchServerlessDestinationDescription = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "CollectionEndpoint" in data:
        out["collection_endpoint"] = data["CollectionEndpoint"]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "BufferingHints" in data:
        import aws_sdk_firehose.types.amazon_open_search_serverless_buffering_hints

        out["buffering_hints"] = (
            aws_sdk_firehose.types.amazon_open_search_serverless_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if "RetryOptions" in data:
        import aws_sdk_firehose.types.amazon_open_search_serverless_retry_options

        out["retry_options"] = (
            aws_sdk_firehose.types.amazon_open_search_serverless_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "S3BackupMode" in data:
        import aws_sdk_firehose.types.amazon_open_search_serverless_s3_backup_mode

        out["s3_backup_mode"] = (
            aws_sdk_firehose.types.amazon_open_search_serverless_s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if "S3DestinationDescription" in data:
        import aws_sdk_firehose.types.s3_destination_description

        out["s3_destination_description"] = (
            aws_sdk_firehose.types.s3_destination_description.deserialize_aws_json_1_1(
                data["S3DestinationDescription"]
            )
        )
    if "ProcessingConfiguration" in data:
        import aws_sdk_firehose.types.processing_configuration

        out["processing_configuration"] = (
            aws_sdk_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if "CloudWatchLoggingOptions" in data:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if "VpcConfigurationDescription" in data:
        import aws_sdk_firehose.types.vpc_configuration_description

        out["vpc_configuration_description"] = (
            aws_sdk_firehose.types.vpc_configuration_description.deserialize_aws_json_1_1(
                data["VpcConfigurationDescription"]
            )
        )
    return out
