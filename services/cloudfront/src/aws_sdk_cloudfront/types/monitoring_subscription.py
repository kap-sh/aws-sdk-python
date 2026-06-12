"""Generated from Smithy shape ``com.amazonaws.cloudfront#MonitoringSubscription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.realtime_metrics_subscription_config


class MonitoringSubscription(TypedDict):
    realtime_metrics_subscription_config: NotRequired[
        "aws_sdk_cloudfront.types.realtime_metrics_subscription_config.RealtimeMetricsSubscriptionConfig"
    ]
    """<p>A subscription configuration for additional CloudWatch metrics.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: MonitoringSubscription, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "realtime_metrics_subscription_config" in value:
        import aws_sdk_cloudfront.types.realtime_metrics_subscription_config

        aws_sdk_cloudfront.types.realtime_metrics_subscription_config.serialize_xml(
            value["realtime_metrics_subscription_config"],
            el,
            "RealtimeMetricsSubscriptionConfig",
        )


def deserialize_xml(el: Element) -> MonitoringSubscription:
    out: MonitoringSubscription = {}  # type: ignore[typeddict-item]
    child_realtime_metrics_subscription_config = el.find(
        "RealtimeMetricsSubscriptionConfig"
    )
    if child_realtime_metrics_subscription_config is not None:
        import aws_sdk_cloudfront.types.realtime_metrics_subscription_config

        out["realtime_metrics_subscription_config"] = (
            aws_sdk_cloudfront.types.realtime_metrics_subscription_config.deserialize_xml(
                child_realtime_metrics_subscription_config
            )
        )
    return out
