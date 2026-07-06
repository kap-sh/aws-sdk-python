"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetMonitoringSubscriptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.monitoring_subscription


class GetMonitoringSubscriptionResult(TypedDict, closed=True):
    monitoring_subscription: NotRequired[
        "aws_sdk_cloudfront.types.monitoring_subscription.MonitoringSubscription"
    ]
    """<p>A monitoring subscription. This structure contains information about whether additional CloudWatch metrics are enabled for a given CloudFront distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetMonitoringSubscriptionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "monitoring_subscription" in value:
        import aws_sdk_cloudfront.types.monitoring_subscription

        aws_sdk_cloudfront.types.monitoring_subscription.serialize_xml(
            value["monitoring_subscription"], el, "MonitoringSubscription"
        )


def deserialize_xml(el: Element) -> GetMonitoringSubscriptionResult:
    out: GetMonitoringSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_monitoring_subscription = el.find("MonitoringSubscription")
    if child_monitoring_subscription is not None:
        import aws_sdk_cloudfront.types.monitoring_subscription

        out["monitoring_subscription"] = (
            aws_sdk_cloudfront.types.monitoring_subscription.deserialize_xml(
                child_monitoring_subscription
            )
        )
    return out
