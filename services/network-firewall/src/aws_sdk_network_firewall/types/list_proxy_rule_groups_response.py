"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListProxyRuleGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.pagination_token
    import aws_sdk_network_firewall.types.proxy_rule_groups


class ListProxyRuleGroupsResponse(TypedDict, closed=True):
    proxy_rule_groups: NotRequired[
        "aws_sdk_network_firewall.types.proxy_rule_groups.ProxyRuleGroups"
    ]
    """<p>The metadata for the proxy rule groups. Depending on your setting for max results and the number of proxy rule groups that you have, this might not be the full list. </p>"""
    next_token: NotRequired[
        "aws_sdk_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProxyRuleGroupsResponse) -> dict:
    out: dict = {}
    if "proxy_rule_groups" in value:
        import aws_sdk_network_firewall.types.proxy_rule_groups

        out["ProxyRuleGroups"] = (
            aws_sdk_network_firewall.types.proxy_rule_groups.serialize_aws_json_1_0(
                value["proxy_rule_groups"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProxyRuleGroupsResponse:
    out: ListProxyRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if "ProxyRuleGroups" in data:
        import aws_sdk_network_firewall.types.proxy_rule_groups

        out["proxy_rule_groups"] = (
            aws_sdk_network_firewall.types.proxy_rule_groups.deserialize_aws_json_1_0(
                data["ProxyRuleGroups"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
