"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverQueryLogConfigAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.count
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.resolver_query_log_config_association_list


class ListResolverQueryLogConfigAssociationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>If there are more than <code>MaxResults</code> query logging associations, you can submit another <code>ListResolverQueryLogConfigAssociations</code> request to get the next group of associations. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""
    total_count: "capo_route53resolver.types.count.Count"
    """<p>The total number of query logging associations that were created by the current account in the specified Region. This count can differ from the number of associations that are returned in a <code>ListResolverQueryLogConfigAssociations</code> response, depending on the values that you specify in the request.</p>"""
    total_filtered_count: "capo_route53resolver.types.count.Count"
    """<p>The total number of query logging associations that were created by the current account in the specified Region and that match the filters that were specified in the <code>ListResolverQueryLogConfigAssociations</code> request. For the total number of associations that were created by the current account in the specified Region, see <code>TotalCount</code>.</p>"""
    resolver_query_log_config_associations: NotRequired[
        "capo_route53resolver.types.resolver_query_log_config_association_list.ResolverQueryLogConfigAssociationList"
    ]
    """<p>A list that contains one <code>ResolverQueryLogConfigAssociations</code> element for each query logging association that matches the values that you specified for <code>Filter</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListResolverQueryLogConfigAssociationsResponse,
) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["TotalCount"] = value.get("total_count", 0)
    out["TotalFilteredCount"] = value.get("total_filtered_count", 0)
    if "resolver_query_log_config_associations" in value:
        import capo_route53resolver.types.resolver_query_log_config_association_list

        out["ResolverQueryLogConfigAssociations"] = (
            capo_route53resolver.types.resolver_query_log_config_association_list.serialize_aws_json_1_1(
                value["resolver_query_log_config_associations"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListResolverQueryLogConfigAssociationsResponse:
    out: ListResolverQueryLogConfigAssociationsResponse = {}  # type: ignore[typeddict-item]
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
    if "ResolverQueryLogConfigAssociations" in data:
        import capo_route53resolver.types.resolver_query_log_config_association_list

        out["resolver_query_log_config_associations"] = (
            capo_route53resolver.types.resolver_query_log_config_association_list.deserialize_aws_json_1_1(
                data["ResolverQueryLogConfigAssociations"]
            )
        )
    return out
