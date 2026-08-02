"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAwsNetworkPerformanceMetricSubscriptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.subscription_list


class DescribeAwsNetworkPerformanceMetricSubscriptionsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    subscriptions: NotRequired["capo_ec2.types.subscription_list.SubscriptionList"]
    """<p>Describes the current Infrastructure Performance subscriptions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAwsNetworkPerformanceMetricSubscriptionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "subscriptions" in value:
        import capo_ec2.types.subscription_list

        capo_ec2.types.subscription_list.serialize_ec2_query(
            value["subscriptions"], pairs, f"{key_prefix}SubscriptionSet"
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeAwsNetworkPerformanceMetricSubscriptionsResult:
    out: DescribeAwsNetworkPerformanceMetricSubscriptionsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("SubscriptionSet") is not None:
        import capo_ec2.types.subscription_list

        out["subscriptions"] = capo_ec2.types.subscription_list.deserialize_ec2_query(
            el, "SubscriptionSet"
        )
    return out
