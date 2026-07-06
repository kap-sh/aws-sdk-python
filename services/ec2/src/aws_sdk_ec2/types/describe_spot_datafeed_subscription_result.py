"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotDatafeedSubscriptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_datafeed_subscription


class DescribeSpotDatafeedSubscriptionResult(TypedDict, closed=True):
    spot_datafeed_subscription: NotRequired[
        "aws_sdk_ec2.types.spot_datafeed_subscription.SpotDatafeedSubscription"
    ]
    """<p>The Spot Instance data feed subscription.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotDatafeedSubscriptionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "spot_datafeed_subscription" in value:
        import aws_sdk_ec2.types.spot_datafeed_subscription

        aws_sdk_ec2.types.spot_datafeed_subscription.serialize_ec2_query(
            value["spot_datafeed_subscription"],
            pairs,
            f"{prefix}.SpotDatafeedSubscription",
        )


def deserialize_ec2_query(el: Element) -> DescribeSpotDatafeedSubscriptionResult:
    out: DescribeSpotDatafeedSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_spot_datafeed_subscription = el.find("SpotDatafeedSubscription")
    if child_spot_datafeed_subscription is not None:
        import aws_sdk_ec2.types.spot_datafeed_subscription

        out["spot_datafeed_subscription"] = (
            aws_sdk_ec2.types.spot_datafeed_subscription.deserialize_ec2_query(
                child_spot_datafeed_subscription
            )
        )
    return out
