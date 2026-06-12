"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonOpenSearchServerlessDestinationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.amazon_open_search_serverless_buffering_hints
    import aws_sdk_firehose.types.amazon_open_search_serverless_collection_endpoint
    import aws_sdk_firehose.types.amazon_open_search_serverless_index_name
    import aws_sdk_firehose.types.amazon_open_search_serverless_retry_options
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.processing_configuration
    import aws_sdk_firehose.types.role_arn
    import aws_sdk_firehose.types.s3_destination_update


class AmazonOpenSearchServerlessDestinationUpdate(TypedDict):
    role_arn: NotRequired["aws_sdk_firehose.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.</p>"""
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
    """<p>The buffering options. If no value is specified, AmazonopensearchBufferingHints object default values are used.</p>"""
    retry_options: NotRequired[
        "aws_sdk_firehose.types.amazon_open_search_serverless_retry_options.AmazonOpenSearchServerlessRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service. The default value is 300 (5 minutes).</p>"""
    s3_update: NotRequired[
        "aws_sdk_firehose.types.s3_destination_update.S3DestinationUpdate"
    ]
    processing_configuration: NotRequired[
        "aws_sdk_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonOpenSearchServerlessDestinationUpdate) -> dict:
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
    if "cloud_watch_logging_options" in value:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonOpenSearchServerlessDestinationUpdate:
    out: AmazonOpenSearchServerlessDestinationUpdate = {}  # type: ignore[typeddict-item]
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
    if "CloudWatchLoggingOptions" in data:
        import aws_sdk_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            aws_sdk_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    return out
