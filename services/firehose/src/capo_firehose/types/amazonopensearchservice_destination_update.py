"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonopensearchserviceDestinationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.amazonopensearchservice_buffering_hints
    import capo_firehose.types.amazonopensearchservice_cluster_endpoint
    import capo_firehose.types.amazonopensearchservice_domain_arn
    import capo_firehose.types.amazonopensearchservice_index_name
    import capo_firehose.types.amazonopensearchservice_index_rotation_period
    import capo_firehose.types.amazonopensearchservice_retry_options
    import capo_firehose.types.amazonopensearchservice_type_name
    import capo_firehose.types.cloud_watch_logging_options
    import capo_firehose.types.document_id_options
    import capo_firehose.types.processing_configuration
    import capo_firehose.types.role_arn
    import capo_firehose.types.s3_destination_update


class AmazonopensearchserviceDestinationUpdate(TypedDict, closed=True):
    role_arn: NotRequired["capo_firehose.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents. </p>"""
    domain_arn: NotRequired[
        "capo_firehose.types.amazonopensearchservice_domain_arn.AmazonopensearchserviceDomainARN"
    ]
    """<p>The ARN of the Amazon OpenSearch Service domain. The IAM role must have permissions for DescribeDomain, DescribeDomains, and DescribeDomainConfig after assuming the IAM role specified in RoleARN.</p>"""
    cluster_endpoint: NotRequired[
        "capo_firehose.types.amazonopensearchservice_cluster_endpoint.AmazonopensearchserviceClusterEndpoint"
    ]
    """<p>The endpoint to use when communicating with the cluster. Specify either this ClusterEndpoint or the DomainARN field. </p>"""
    index_name: NotRequired[
        "capo_firehose.types.amazonopensearchservice_index_name.AmazonopensearchserviceIndexName"
    ]
    """<p>The Amazon OpenSearch Service index name.</p>"""
    type_name: NotRequired[
        "capo_firehose.types.amazonopensearchservice_type_name.AmazonopensearchserviceTypeName"
    ]
    """<p>The Amazon OpenSearch Service type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Firehose returns an error during runtime. </p> <p>If you upgrade Elasticsearch from 6.x to 7.x and don’t update your Firehose stream, Firehose still delivers data to Elasticsearch with the old index name and type name. If you want to update your Firehose stream with a new index name, provide an empty string for TypeName. </p>"""
    index_rotation_period: NotRequired[
        "capo_firehose.types.amazonopensearchservice_index_rotation_period.AmazonopensearchserviceIndexRotationPeriod"
    ]
    """<p>The Amazon OpenSearch Service index rotation period. Index rotation appends a timestamp to IndexName to facilitate the expiration of old data.</p>"""
    buffering_hints: NotRequired[
        "capo_firehose.types.amazonopensearchservice_buffering_hints.AmazonopensearchserviceBufferingHints"
    ]
    """<p>The buffering options. If no value is specified, AmazonopensearchBufferingHints object default values are used. </p>"""
    retry_options: NotRequired[
        "capo_firehose.types.amazonopensearchservice_retry_options.AmazonopensearchserviceRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes). </p>"""
    s3_update: NotRequired[
        "capo_firehose.types.s3_destination_update.S3DestinationUpdate"
    ]
    processing_configuration: NotRequired[
        "capo_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    cloud_watch_logging_options: NotRequired[
        "capo_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    document_id_options: NotRequired[
        "capo_firehose.types.document_id_options.DocumentIdOptions"
    ]
    """<p>Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonopensearchserviceDestinationUpdate) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "domain_arn" in value:
        out["DomainARN"] = value["domain_arn"]
    if "cluster_endpoint" in value:
        out["ClusterEndpoint"] = value["cluster_endpoint"]
    if "index_name" in value:
        out["IndexName"] = value["index_name"]
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "index_rotation_period" in value:
        import capo_firehose.types.amazonopensearchservice_index_rotation_period

        out["IndexRotationPeriod"] = (
            capo_firehose.types.amazonopensearchservice_index_rotation_period.serialize_aws_json_1_1(
                value["index_rotation_period"]
            )
        )
    if "buffering_hints" in value:
        import capo_firehose.types.amazonopensearchservice_buffering_hints

        out["BufferingHints"] = (
            capo_firehose.types.amazonopensearchservice_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "retry_options" in value:
        import capo_firehose.types.amazonopensearchservice_retry_options

        out["RetryOptions"] = (
            capo_firehose.types.amazonopensearchservice_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_update" in value:
        import capo_firehose.types.s3_destination_update

        out["S3Update"] = (
            capo_firehose.types.s3_destination_update.serialize_aws_json_1_1(
                value["s3_update"]
            )
        )
    if "processing_configuration" in value:
        import capo_firehose.types.processing_configuration

        out["ProcessingConfiguration"] = (
            capo_firehose.types.processing_configuration.serialize_aws_json_1_1(
                value["processing_configuration"]
            )
        )
    if "cloud_watch_logging_options" in value:
        import capo_firehose.types.cloud_watch_logging_options

        out["CloudWatchLoggingOptions"] = (
            capo_firehose.types.cloud_watch_logging_options.serialize_aws_json_1_1(
                value["cloud_watch_logging_options"]
            )
        )
    if "document_id_options" in value:
        import capo_firehose.types.document_id_options

        out["DocumentIdOptions"] = (
            capo_firehose.types.document_id_options.serialize_aws_json_1_1(
                value["document_id_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AmazonopensearchserviceDestinationUpdate:
    out: AmazonopensearchserviceDestinationUpdate = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "DomainARN" in data:
        out["domain_arn"] = data["DomainARN"]
    if "ClusterEndpoint" in data:
        out["cluster_endpoint"] = data["ClusterEndpoint"]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "IndexRotationPeriod" in data:
        import capo_firehose.types.amazonopensearchservice_index_rotation_period

        out["index_rotation_period"] = (
            capo_firehose.types.amazonopensearchservice_index_rotation_period.deserialize_aws_json_1_1(
                data["IndexRotationPeriod"]
            )
        )
    if "BufferingHints" in data:
        import capo_firehose.types.amazonopensearchservice_buffering_hints

        out["buffering_hints"] = (
            capo_firehose.types.amazonopensearchservice_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if "RetryOptions" in data:
        import capo_firehose.types.amazonopensearchservice_retry_options

        out["retry_options"] = (
            capo_firehose.types.amazonopensearchservice_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "S3Update" in data:
        import capo_firehose.types.s3_destination_update

        out["s3_update"] = (
            capo_firehose.types.s3_destination_update.deserialize_aws_json_1_1(
                data["S3Update"]
            )
        )
    if "ProcessingConfiguration" in data:
        import capo_firehose.types.processing_configuration

        out["processing_configuration"] = (
            capo_firehose.types.processing_configuration.deserialize_aws_json_1_1(
                data["ProcessingConfiguration"]
            )
        )
    if "CloudWatchLoggingOptions" in data:
        import capo_firehose.types.cloud_watch_logging_options

        out["cloud_watch_logging_options"] = (
            capo_firehose.types.cloud_watch_logging_options.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptions"]
            )
        )
    if "DocumentIdOptions" in data:
        import capo_firehose.types.document_id_options

        out["document_id_options"] = (
            capo_firehose.types.document_id_options.deserialize_aws_json_1_1(
                data["DocumentIdOptions"]
            )
        )
    return out
