"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribeInstanceTypeLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.domain_name
    import aws_sdk_opensearch.types.open_search_partition_instance_type
    import aws_sdk_opensearch.types.version_string


class DescribeInstanceTypeLimitsRequest(TypedDict, closed=True):
    domain_name: NotRequired["aws_sdk_opensearch.types.domain_name.DomainName"]
    """<p>The name of the domain. Only specify if you need the limits for an existing domain.</p>"""
    instance_type: "aws_sdk_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType"
    """<p>The OpenSearch Service instance type for which you need limit information.</p>"""
    engine_version: "aws_sdk_opensearch.types.version_string.VersionString"
    """<p>Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInstanceTypeLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeInstanceTypeLimitsRequest:
    out: DescribeInstanceTypeLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
