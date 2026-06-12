"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverQueryLogConfigsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.count
    import aws_sdk_route53resolver.types.next_token
    import aws_sdk_route53resolver.types.resolver_query_log_config_list


class ListResolverQueryLogConfigsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_route53resolver.types.next_token.NextToken"]
    """<p>If there are more than <code>MaxResults</code> query logging configurations, you can submit another <code>ListResolverQueryLogConfigs</code> request to get the next group of configurations. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""
    total_count: "aws_sdk_route53resolver.types.count.Count"
    """<p>The total number of query logging configurations that were created by the current account in the specified Region. This count can differ from the number of query logging configurations that are returned in a <code>ListResolverQueryLogConfigs</code> response, depending on the values that you specify in the request.</p>"""
    total_filtered_count: "aws_sdk_route53resolver.types.count.Count"
    """<p>The total number of query logging configurations that were created by the current account in the specified Region and that match the filters that were specified in the <code>ListResolverQueryLogConfigs</code> request. For the total number of query logging configurations that were created by the current account in the specified Region, see <code>TotalCount</code>.</p>"""
    resolver_query_log_configs: NotRequired[
        "aws_sdk_route53resolver.types.resolver_query_log_config_list.ResolverQueryLogConfigList"
    ]
    """<p>A list that contains one <code>ResolverQueryLogConfig</code> element for each query logging configuration that matches the values that you specified for <code>Filter</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverQueryLogConfigsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["TotalCount"] = value.get("total_count", 0)
    out["TotalFilteredCount"] = value.get("total_filtered_count", 0)
    if "resolver_query_log_configs" in value:
        import aws_sdk_route53resolver.types.resolver_query_log_config_list

        out["ResolverQueryLogConfigs"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_list.serialize_aws_json_1_1(
                value["resolver_query_log_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverQueryLogConfigsResponse:
    out: ListResolverQueryLogConfigsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    else:
        out["total_count"] = 0
    if "TotalFilteredCount" in data:
        out["total_filtered_count"] = data["TotalFilteredCount"]
    else:
        out["total_filtered_count"] = 0
    if "ResolverQueryLogConfigs" in data:
        import aws_sdk_route53resolver.types.resolver_query_log_config_list

        out["resolver_query_log_configs"] = (
            aws_sdk_route53resolver.types.resolver_query_log_config_list.deserialize_aws_json_1_1(
                data["ResolverQueryLogConfigs"]
            )
        )
    return out
