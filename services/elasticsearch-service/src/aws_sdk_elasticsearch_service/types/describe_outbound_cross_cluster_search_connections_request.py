"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribeOutboundCrossClusterSearchConnectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.filter_list
    import aws_sdk_elasticsearch_service.types.max_results
    import aws_sdk_elasticsearch_service.types.next_token


class DescribeOutboundCrossClusterSearchConnectionsRequest(TypedDict, closed=True):
    filters: NotRequired["aws_sdk_elasticsearch_service.types.filter_list.FilterList"]
    """<p> A list of filters used to match properties for outbound cross-cluster search connection. Available <code><a>Filter</a></code> names for this operation are: <ul> <li>cross-cluster-search-connection-id</li> <li>destination-domain-info.domain-name</li> <li>destination-domain-info.owner-id</li> <li>destination-domain-info.region</li> <li>source-domain-info.domain-name</li> </ul> </p>"""
    max_results: "aws_sdk_elasticsearch_service.types.max_results.MaxResults"
    """<p>Set this value to limit the number of results returned. If not specified, defaults to 100.</p>"""
    next_token: NotRequired["aws_sdk_elasticsearch_service.types.next_token.NextToken"]
    """<p> NextToken is sent in case the earlier API call results contain the NextToken. It is used for pagination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOutboundCrossClusterSearchConnectionsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_elasticsearch_service.types.filter_list

        out["Filters"] = aws_sdk_elasticsearch_service.types.filter_list.serialize_json(
            value["filters"]
        )
    out["MaxResults"] = value.get("max_results", 0)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> DescribeOutboundCrossClusterSearchConnectionsRequest:
    out: DescribeOutboundCrossClusterSearchConnectionsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_elasticsearch_service.types.filter_list

        out["filters"] = (
            aws_sdk_elasticsearch_service.types.filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
