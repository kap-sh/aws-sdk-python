"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeElasticsearchInstanceTypeLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.domain_name
    import aws_sdk_elasticsearch_service.types.elasticsearch_version_string
    import aws_sdk_elasticsearch_service.types.es_partition_instance_type


class DescribeElasticsearchInstanceTypeLimitsRequest(TypedDict, closed=True):
    domain_name: NotRequired[
        "aws_sdk_elasticsearch_service.types.domain_name.DomainName"
    ]
    """<p> DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch <code> <a>Limits</a> </code> for existing domain. </p>"""
    instance_type: "aws_sdk_elasticsearch_service.types.es_partition_instance_type.ESPartitionInstanceType"
    """<p> The instance type for an Elasticsearch cluster for which Elasticsearch <code> <a>Limits</a> </code> are needed. </p>"""
    elasticsearch_version: "aws_sdk_elasticsearch_service.types.elasticsearch_version_string.ElasticsearchVersionString"
    """<p> Version of Elasticsearch for which <code> <a>Limits</a> </code> are needed. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeElasticsearchInstanceTypeLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeElasticsearchInstanceTypeLimitsRequest:
    out: DescribeElasticsearchInstanceTypeLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
