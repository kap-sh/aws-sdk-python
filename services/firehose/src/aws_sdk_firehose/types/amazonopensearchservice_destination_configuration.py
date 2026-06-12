"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonopensearchserviceDestinationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_firehose.types.amazonopensearchservice_buffering_hints
    import aws_sdk_firehose.types.amazonopensearchservice_cluster_endpoint
    import aws_sdk_firehose.types.amazonopensearchservice_domain_arn
    import aws_sdk_firehose.types.amazonopensearchservice_index_name
    import aws_sdk_firehose.types.amazonopensearchservice_index_rotation_period
    import aws_sdk_firehose.types.amazonopensearchservice_retry_options
    import aws_sdk_firehose.types.amazonopensearchservice_s3_backup_mode
    import aws_sdk_firehose.types.amazonopensearchservice_type_name
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.document_id_options
    import aws_sdk_firehose.types.processing_configuration
    import aws_sdk_firehose.types.role_arn
    import aws_sdk_firehose.types.s3_destination_configuration
    import aws_sdk_firehose.types.vpc_configuration


class AmazonopensearchserviceDestinationConfiguration(TypedDict):
    role_arn: "aws_sdk_firehose.types.role_arn.RoleARN"
    """<p>The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents.</p>"""
    domain_arn: NotRequired[
        "aws_sdk_firehose.types.amazonopensearchservice_domain_arn.AmazonopensearchserviceDomainARN"
    ]
    """<p>The ARN of the Amazon OpenSearch Service domain. The IAM role must have permissions for DescribeElasticsearchDomain, DescribeElasticsearchDomains, and DescribeElasticsearchDomainConfig after assuming the role specified in RoleARN. </p>"""
    cluster_endpoint: NotRequired[
        "aws_sdk_firehose.types.amazonopensearchservice_cluster_endpoint.AmazonopensearchserviceClusterEndpoint"
    ]
    """<p>The endpoint to use when communicating with the cluster. Specify either this ClusterEndpoint or the DomainARN field. </p>"""
    index_name: "aws_sdk_firehose.types.amazonopensearchservice_index_name.AmazonopensearchserviceIndexName"
    """<p>The ElasticsearAmazon OpenSearch Service index name.</p>"""
    type_name: NotRequired[
        "aws_sdk_firehose.types.amazonopensearchservice_type_name.AmazonopensearchserviceTypeName"
    ]
    """<p>The Amazon OpenSearch Service type name. For Elasticsearch 6.x, there can be only one type per index. If you try to specify a new type for an existing index that already has another type, Firehose returns an error during run time. </p>"""
    index_rotation_period: NotRequired[
        "aws_sdk_firehose.types.amazonopensearchservice_index_rotation_period.AmazonopensearchserviceIndexRotationPeriod"
    ]
    """<p>The Amazon OpenSearch Service index rotation period. Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data.</p>"""
    buffering_hints: NotRequired[
        "aws_sdk_firehose.types.amazonopensearchservice_buffering_hints.AmazonopensearchserviceBufferingHints"
    ]
    """<p>The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used. </p>"""
    retry_options: NotRequired[
        "aws_sdk_firehose.types.amazonopensearchservice_retry_options.AmazonopensearchserviceRetryOptions"
    ]
    """<p>The retry behavior in case Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes). </p>"""
    s3_backup_mode: NotRequired[
        "aws_sdk_firehose.types.amazonopensearchservice_s3_backup_mode.AmazonopensearchserviceS3BackupMode"
    ]
    """<p>Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix. </p>"""
    s3_configuration: (
        "aws_sdk_firehose.types.s3_destination_configuration.S3DestinationConfiguration"
    )
    processing_configuration: NotRequired[
        "aws_sdk_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    vpc_configuration: NotRequired[
        "aws_sdk_firehose.types.vpc_configuration.VpcConfiguration"
    ]
    document_id_options: NotRequired[
        "aws_sdk_firehose.types.document_id_options.DocumentIdOptions"
    ]
    """<p>Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AmazonopensearchserviceDestinationConfiguration,
) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    if "domain_arn" in value:
        out["DomainARN"] = value["domain_arn"]
    if "cluster_endpoint" in value:
        out["ClusterEndpoint"] = value["cluster_endpoint"]
    out["IndexName"] = value["index_name"]
    if "type_name" in value:
        out["TypeName"] = value["type_name"]
    if "index_rotation_period" in value:
        import aws_sdk_firehose.types.amazonopensearchservice_index_rotation_period

        out["IndexRotationPeriod"] = (
            aws_sdk_firehose.types.amazonopensearchservice_index_rotation_period.serialize_aws_json_1_1(
                value["index_rotation_period"]
            )
        )
    if "buffering_hints" in value:
        import aws_sdk_firehose.types.amazonopensearchservice_buffering_hints

        out["BufferingHints"] = (
            aws_sdk_firehose.types.amazonopensearchservice_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "retry_options" in value:
        import aws_sdk_firehose.types.amazonopensearchservice_retry_options

        out["RetryOptions"] = (
            aws_sdk_firehose.types.amazonopensearchservice_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import aws_sdk_firehose.types.amazonopensearchservice_s3_backup_mode

        out["S3BackupMode"] = (
            aws_sdk_firehose.types.amazonopensearchservice_s3_backup_mode.serialize_aws_json_1_1(
                value["s3_backup_mode"]
            )
        )
    import aws_sdk_firehose.types.s3_destination_configuration

    out["S3Configuration"] = (
        aws_sdk_firehose.types.s3_destination_configuration.serialize_aws_json_1_1(
            value["s3_configuration"]
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
    if "vpc_configuration" in value:
        import aws_sdk_firehose.types.vpc_configuration

        out["VpcConfiguration"] = (
            aws_sdk_firehose.types.vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    if "document_id_options" in value:
        import aws_sdk_firehose.types.document_id_options

        out["DocumentIdOptions"] = (
            aws_sdk_firehose.types.document_id_options.serialize_aws_json_1_1(
                value["document_id_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AmazonopensearchserviceDestinationConfiguration:
    out: AmazonopensearchserviceDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    else:
        raise DeserializationError(
            "AmazonopensearchserviceDestinationConfiguration.role_arn required"
        )
    if "DomainARN" in data:
        out["domain_arn"] = data["DomainARN"]
    if "ClusterEndpoint" in data:
        out["cluster_endpoint"] = data["ClusterEndpoint"]
    if "IndexName" in data:
        out["index_name"] = data["IndexName"]
    else:
        raise DeserializationError(
            "AmazonopensearchserviceDestinationConfiguration.index_name required"
        )
    if "TypeName" in data:
        out["type_name"] = data["TypeName"]
    if "IndexRotationPeriod" in data:
        import aws_sdk_firehose.types.amazonopensearchservice_index_rotation_period

        out["index_rotation_period"] = (
            aws_sdk_firehose.types.amazonopensearchservice_index_rotation_period.deserialize_aws_json_1_1(
                data["IndexRotationPeriod"]
            )
        )
    if "BufferingHints" in data:
        import aws_sdk_firehose.types.amazonopensearchservice_buffering_hints

        out["buffering_hints"] = (
            aws_sdk_firehose.types.amazonopensearchservice_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if "RetryOptions" in data:
        import aws_sdk_firehose.types.amazonopensearchservice_retry_options

        out["retry_options"] = (
            aws_sdk_firehose.types.amazonopensearchservice_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "S3BackupMode" in data:
        import aws_sdk_firehose.types.amazonopensearchservice_s3_backup_mode

        out["s3_backup_mode"] = (
            aws_sdk_firehose.types.amazonopensearchservice_s3_backup_mode.deserialize_aws_json_1_1(
                data["S3BackupMode"]
            )
        )
    if "S3Configuration" in data:
        import aws_sdk_firehose.types.s3_destination_configuration

        out["s3_configuration"] = (
            aws_sdk_firehose.types.s3_destination_configuration.deserialize_aws_json_1_1(
                data["S3Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "AmazonopensearchserviceDestinationConfiguration.s3_configuration required"
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
    if "VpcConfiguration" in data:
        import aws_sdk_firehose.types.vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_firehose.types.vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    if "DocumentIdOptions" in data:
        import aws_sdk_firehose.types.document_id_options

        out["document_id_options"] = (
            aws_sdk_firehose.types.document_id_options.deserialize_aws_json_1_1(
                data["DocumentIdOptions"]
            )
        )
    return out
