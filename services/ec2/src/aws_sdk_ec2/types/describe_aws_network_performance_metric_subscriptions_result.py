"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeAwsNetworkPerformanceMetricSubscriptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subscription_list


class DescribeAwsNetworkPerformanceMetricSubscriptionsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    subscriptions: NotRequired["aws_sdk_ec2.types.subscription_list.SubscriptionList"]
    """<p>Describes the current Infrastructure Performance subscriptions.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeAwsNetworkPerformanceMetricSubscriptionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "subscriptions" in value:
        import aws_sdk_ec2.types.subscription_list

        aws_sdk_ec2.types.subscription_list.serialize_ec2_query(
            value["subscriptions"], pairs, f"{prefix}.SubscriptionSet"
        )


def deserialize_ec2_query(
    el: Element,
) -> DescribeAwsNetworkPerformanceMetricSubscriptionsResult:
    out: DescribeAwsNetworkPerformanceMetricSubscriptionsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("SubscriptionSet") is not None:
        import aws_sdk_ec2.types.subscription_list

        out["subscriptions"] = (
            aws_sdk_ec2.types.subscription_list.deserialize_ec2_query(
                el, "SubscriptionSet"
            )
        )
    return out
