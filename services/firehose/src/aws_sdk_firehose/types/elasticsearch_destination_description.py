"""Generated from Smithy shape ``com.amazonaws.firehose#ElasticsearchDestinationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.cloud_watch_logging_options
    import aws_sdk_firehose.types.document_id_options
    import aws_sdk_firehose.types.elasticsearch_buffering_hints
    import aws_sdk_firehose.types.elasticsearch_cluster_endpoint
    import aws_sdk_firehose.types.elasticsearch_domain_arn
    import aws_sdk_firehose.types.elasticsearch_index_name
    import aws_sdk_firehose.types.elasticsearch_index_rotation_period
    import aws_sdk_firehose.types.elasticsearch_retry_options
    import aws_sdk_firehose.types.elasticsearch_s3_backup_mode
    import aws_sdk_firehose.types.elasticsearch_type_name
    import aws_sdk_firehose.types.processing_configuration
    import aws_sdk_firehose.types.role_arn
    import aws_sdk_firehose.types.s3_destination_description
    import aws_sdk_firehose.types.vpc_configuration_description


class ElasticsearchDestinationDescription(TypedDict):
    role_arn: NotRequired["aws_sdk_firehose.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p>"""
    domain_arn: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_domain_arn.ElasticsearchDomainARN"
    ]
    """<p>The ARN of the Amazon OpenSearch Service domain. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a>.</p> <p>Firehose uses either <code>ClusterEndpoint</code> or <code>DomainARN</code> to send data to Amazon OpenSearch Service.</p>"""
    cluster_endpoint: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_cluster_endpoint.ElasticsearchClusterEndpoint"
    ]
    """<p>The endpoint to use when communicating with the cluster. Firehose uses either this <code>ClusterEndpoint</code> or the <code>DomainARN</code> field to send data to Amazon OpenSearch Service.</p>"""
    index_name: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_index_name.ElasticsearchIndexName"
    ]
    """<p>The Elasticsearch index name.</p>"""
    type_name: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_type_name.ElasticsearchTypeName"
    ]
    """<p>The Elasticsearch type name. This applies to Elasticsearch 6.x and lower versions. For Elasticsearch 7.x and OpenSearch Service 1.x, there's no value for <code>TypeName</code>.</p>"""
    index_rotation_period: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_index_rotation_period.ElasticsearchIndexRotationPeriod"
    ]
    """<p>The Elasticsearch index rotation period</p>"""
    buffering_hints: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_buffering_hints.ElasticsearchBufferingHints"
    ]
    """<p>The buffering options.</p>"""
    retry_options: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_retry_options.ElasticsearchRetryOptions"
    ]
    """<p>The Amazon OpenSearch Service retry options.</p>"""
    s3_backup_mode: NotRequired[
        "aws_sdk_firehose.types.elasticsearch_s3_backup_mode.ElasticsearchS3BackupMode"
    ]
    """<p>The Amazon S3 backup mode.</p>"""
    s3_destination_description: NotRequired[
        "aws_sdk_firehose.types.s3_destination_description.S3DestinationDescription"
    ]
    """<p>The Amazon S3 destination.</p>"""
    processing_configuration: NotRequired[
        "aws_sdk_firehose.types.processing_configuration.ProcessingConfiguration"
    ]
    """<p>The data processing configuration.</p>"""
    cloud_watch_logging_options: NotRequired[
        "aws_sdk_firehose.types.cloud_watch_logging_options.CloudWatchLoggingOptions"
    ]
    """<p>The Amazon CloudWatch logging options.</p>"""
    vpc_configuration_description: NotRequired[
        "aws_sdk_firehose.types.vpc_configuration_description.VpcConfigurationDescription"
    ]
    """<p>The details of the VPC of the Amazon OpenSearch or the Amazon OpenSearch Serverless destination.</p>"""
    document_id_options: NotRequired[
        "aws_sdk_firehose.types.document_id_options.DocumentIdOptions"
    ]
    """<p>Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ElasticsearchDestinationDescription) -> dict:
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
        import aws_sdk_firehose.types.elasticsearch_index_rotation_period

        out["IndexRotationPeriod"] = (
            aws_sdk_firehose.types.elasticsearch_index_rotation_period.serialize_aws_json_1_1(
                value["index_rotation_period"]
            )
        )
    if "buffering_hints" in value:
        import aws_sdk_firehose.types.elasticsearch_buffering_hints

        out["BufferingHints"] = (
            aws_sdk_firehose.types.elasticsearch_buffering_hints.serialize_aws_json_1_1(
                value["buffering_hints"]
            )
        )
    if "retry_options" in value:
        import aws_sdk_firehose.types.elasticsearch_retry_options

        out["RetryOptions"] = (
            aws_sdk_firehose.types.elasticsearch_retry_options.serialize_aws_json_1_1(
                value["retry_options"]
            )
        )
    if "s3_backup_mode" in value:
        import aws_sdk_firehose.types.elasticsearch_s3_backup_mode

        out["S3BackupMode"] = (
            aws_sdk_firehose.types.elasticsearch_s3_backup_mode.serialize_aws_json_1_1(
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
    if "document_id_options" in value:
        import aws_sdk_firehose.types.document_id_options

        out["DocumentIdOptions"] = (
            aws_sdk_firehose.types.document_id_options.serialize_aws_json_1_1(
                value["document_id_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ElasticsearchDestinationDescription:
    out: ElasticsearchDestinationDescription = {}  # type: ignore[typeddict-item]
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
        import aws_sdk_firehose.types.elasticsearch_index_rotation_period

        out["index_rotation_period"] = (
            aws_sdk_firehose.types.elasticsearch_index_rotation_period.deserialize_aws_json_1_1(
                data["IndexRotationPeriod"]
            )
        )
    if "BufferingHints" in data:
        import aws_sdk_firehose.types.elasticsearch_buffering_hints

        out["buffering_hints"] = (
            aws_sdk_firehose.types.elasticsearch_buffering_hints.deserialize_aws_json_1_1(
                data["BufferingHints"]
            )
        )
    if "RetryOptions" in data:
        import aws_sdk_firehose.types.elasticsearch_retry_options

        out["retry_options"] = (
            aws_sdk_firehose.types.elasticsearch_retry_options.deserialize_aws_json_1_1(
                data["RetryOptions"]
            )
        )
    if "S3BackupMode" in data:
        import aws_sdk_firehose.types.elasticsearch_s3_backup_mode

        out["s3_backup_mode"] = (
            aws_sdk_firehose.types.elasticsearch_s3_backup_mode.deserialize_aws_json_1_1(
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
    if "DocumentIdOptions" in data:
        import aws_sdk_firehose.types.document_id_options

        out["document_id_options"] = (
            aws_sdk_firehose.types.document_id_options.deserialize_aws_json_1_1(
                data["DocumentIdOptions"]
            )
        )
    return out
