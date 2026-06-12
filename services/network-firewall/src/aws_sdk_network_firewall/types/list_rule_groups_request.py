"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListRuleGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.pagination_max_results
    import aws_sdk_network_firewall.types.pagination_token
    import aws_sdk_network_firewall.types.resource_managed_status
    import aws_sdk_network_firewall.types.resource_managed_type
    import aws_sdk_network_firewall.types.rule_group_type
    import aws_sdk_network_firewall.types.subscription_status


class ListRuleGroupsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    max_results: NotRequired[
        "aws_sdk_network_firewall.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    scope: NotRequired[
        "aws_sdk_network_firewall.types.resource_managed_status.ResourceManagedStatus"
    ]
    """<p>The scope of the request. The default setting of <code>ACCOUNT</code> or a setting of <code>NULL</code> returns all of the rule groups in your account. A setting of <code>MANAGED</code> returns all available managed rule groups.</p>"""
    managed_type: NotRequired[
        "aws_sdk_network_firewall.types.resource_managed_type.ResourceManagedType"
    ]
    """<p>Indicates the general category of the Amazon Web Services managed rule group.</p>"""
    subscription_status: NotRequired[
        "aws_sdk_network_firewall.types.subscription_status.SubscriptionStatus"
    ]
    """<p>Filters the results to show only rule groups with the specified subscription status. Use this to find subscribed or unsubscribed rule groups.</p>"""
    type: NotRequired["aws_sdk_network_firewall.types.rule_group_type.RuleGroupType"]
    """<p>Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRuleGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "scope" in value:
        import aws_sdk_network_firewall.types.resource_managed_status

        out["Scope"] = (
            aws_sdk_network_firewall.types.resource_managed_status.serialize_aws_json_1_0(
                value["scope"]
            )
        )
    if "managed_type" in value:
        import aws_sdk_network_firewall.types.resource_managed_type

        out["ManagedType"] = (
            aws_sdk_network_firewall.types.resource_managed_type.serialize_aws_json_1_0(
                value["managed_type"]
            )
        )
    if "subscription_status" in value:
        import aws_sdk_network_firewall.types.subscription_status

        out["SubscriptionStatus"] = (
            aws_sdk_network_firewall.types.subscription_status.serialize_aws_json_1_0(
                value["subscription_status"]
            )
        )
    if "type" in value:
        import aws_sdk_network_firewall.types.rule_group_type

        out["Type"] = (
            aws_sdk_network_firewall.types.rule_group_type.serialize_aws_json_1_0(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRuleGroupsRequest:
    out: ListRuleGroupsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Scope" in data:
        import aws_sdk_network_firewall.types.resource_managed_status

        out["scope"] = (
            aws_sdk_network_firewall.types.resource_managed_status.deserialize_aws_json_1_0(
                data["Scope"]
            )
        )
    if "ManagedType" in data:
        import aws_sdk_network_firewall.types.resource_managed_type

        out["managed_type"] = (
            aws_sdk_network_firewall.types.resource_managed_type.deserialize_aws_json_1_0(
                data["ManagedType"]
            )
        )
    if "SubscriptionStatus" in data:
        import aws_sdk_network_firewall.types.subscription_status

        out["subscription_status"] = (
            aws_sdk_network_firewall.types.subscription_status.deserialize_aws_json_1_0(
                data["SubscriptionStatus"]
            )
        )
    if "Type" in data:
        import aws_sdk_network_firewall.types.rule_group_type

        out["type"] = (
            aws_sdk_network_firewall.types.rule_group_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    return out
