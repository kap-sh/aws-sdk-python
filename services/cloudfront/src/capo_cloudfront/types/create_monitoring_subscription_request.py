"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateMonitoringSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.monitoring_subscription
    import capo_cloudfront.types.string


class CreateMonitoringSubscriptionRequest(TypedDict, closed=True):
    distribution_id: "capo_cloudfront.types.string.string"
    """<p>The ID of the distribution that you are enabling metrics for.</p>"""
    monitoring_subscription: (
        "capo_cloudfront.types.monitoring_subscription.MonitoringSubscription"
    )
    """<p>A monitoring subscription. This structure contains information about whether additional CloudWatch metrics are enabled for a given CloudFront distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateMonitoringSubscriptionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.monitoring_subscription

    capo_cloudfront.types.monitoring_subscription.serialize_xml(
        value["monitoring_subscription"], el, "MonitoringSubscription"
    )


def deserialize_xml(el: Element) -> CreateMonitoringSubscriptionRequest:
    out: CreateMonitoringSubscriptionRequest = {}  # type: ignore[typeddict-item]
    child_monitoring_subscription = el.find("MonitoringSubscription")
    if child_monitoring_subscription is not None:
        import capo_cloudfront.types.monitoring_subscription

        out["monitoring_subscription"] = (
            capo_cloudfront.types.monitoring_subscription.deserialize_xml(
                child_monitoring_subscription
            )
        )
    else:
        raise DeserializationError(
            "CreateMonitoringSubscriptionRequest.monitoring_subscription required"
        )
    return out
