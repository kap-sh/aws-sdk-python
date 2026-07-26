"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateMonitoringSubscriptionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.monitoring_subscription


class CreateMonitoringSubscriptionResult(TypedDict, closed=True):
    monitoring_subscription: NotRequired[
        "capo_cloudfront.types.monitoring_subscription.MonitoringSubscription"
    ]
    """<p>A monitoring subscription. This structure contains information about whether additional CloudWatch metrics are enabled for a given CloudFront distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateMonitoringSubscriptionResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "monitoring_subscription" in value:
        import capo_cloudfront.types.monitoring_subscription

        capo_cloudfront.types.monitoring_subscription.serialize_xml(
            value["monitoring_subscription"], el, "MonitoringSubscription"
        )


def deserialize_xml(el: Element) -> CreateMonitoringSubscriptionResult:
    out: CreateMonitoringSubscriptionResult = {}  # type: ignore[typeddict-item]
    child_monitoring_subscription = el.find("MonitoringSubscription")
    if child_monitoring_subscription is not None:
        import capo_cloudfront.types.monitoring_subscription

        out["monitoring_subscription"] = (
            capo_cloudfront.types.monitoring_subscription.deserialize_xml(
                child_monitoring_subscription
            )
        )
    return out
