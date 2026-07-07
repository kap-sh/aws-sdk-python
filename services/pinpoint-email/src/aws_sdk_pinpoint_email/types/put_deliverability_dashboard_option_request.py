"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutDeliverabilityDashboardOptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.domain_deliverability_tracking_options
    import aws_sdk_pinpoint_email.types.enabled


class PutDeliverabilityDashboardOptionRequest(TypedDict, closed=True):
    dashboard_enabled: "aws_sdk_pinpoint_email.types.enabled.Enabled"
    """<p>Specifies whether to enable the Deliverability dashboard for your Amazon Pinpoint account. To enable the dashboard, set this value to <code>true</code>.</p>"""
    subscribed_domains: NotRequired[
        "aws_sdk_pinpoint_email.types.domain_deliverability_tracking_options.DomainDeliverabilityTrackingOptions"
    ]
    """<p>An array of objects, one for each verified domain that you use to send email and enabled the Deliverability dashboard for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDeliverabilityDashboardOptionRequest) -> dict:
    out: dict = {}
    out["DashboardEnabled"] = value.get("dashboard_enabled", False)
    if "subscribed_domains" in value:
        import aws_sdk_pinpoint_email.types.domain_deliverability_tracking_options

        out["SubscribedDomains"] = (
            aws_sdk_pinpoint_email.types.domain_deliverability_tracking_options.serialize_json(
                value["subscribed_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutDeliverabilityDashboardOptionRequest:
    out: PutDeliverabilityDashboardOptionRequest = {}  # type: ignore[typeddict-item]
    if "DashboardEnabled" in data:
        out["dashboard_enabled"] = data["DashboardEnabled"]
    else:
        out["dashboard_enabled"] = False
    if "SubscribedDomains" in data:
        import aws_sdk_pinpoint_email.types.domain_deliverability_tracking_options

        out["subscribed_domains"] = (
            aws_sdk_pinpoint_email.types.domain_deliverability_tracking_options.deserialize_json(
                data["SubscribedDomains"]
            )
        )
    return out
