"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetDeliverabilityDashboardOptionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.deliverability_dashboard_account_status
    import capo_pinpoint_email.types.domain_deliverability_tracking_options
    import capo_pinpoint_email.types.enabled
    import capo_pinpoint_email.types.timestamp


class GetDeliverabilityDashboardOptionsResponse(TypedDict, closed=True):
    dashboard_enabled: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Specifies whether the Deliverability dashboard is enabled for your Amazon Pinpoint account. If this value is <code>true</code>, the dashboard is enabled.</p>"""
    subscription_expiry_date: NotRequired[
        "capo_pinpoint_email.types.timestamp.Timestamp"
    ]
    """<p>The date, in Unix time format, when your current subscription to the Deliverability dashboard is scheduled to expire, if your subscription is scheduled to expire at the end of the current calendar month. This value is null if you have an active subscription that isn’t due to expire at the end of the month.</p>"""
    account_status: NotRequired[
        "capo_pinpoint_email.types.deliverability_dashboard_account_status.DeliverabilityDashboardAccountStatus"
    ]
    """<p>The current status of your Deliverability dashboard subscription. If this value is <code>PENDING_EXPIRATION</code>, your subscription is scheduled to expire at the end of the current calendar month.</p>"""
    active_subscribed_domains: NotRequired[
        "capo_pinpoint_email.types.domain_deliverability_tracking_options.DomainDeliverabilityTrackingOptions"
    ]
    """<p>An array of objects, one for each verified domain that you use to send email and currently has an active Deliverability dashboard subscription that isn’t scheduled to expire at the end of the current calendar month.</p>"""
    pending_expiration_subscribed_domains: NotRequired[
        "capo_pinpoint_email.types.domain_deliverability_tracking_options.DomainDeliverabilityTrackingOptions"
    ]
    """<p>An array of objects, one for each verified domain that you use to send email and currently has an active Deliverability dashboard subscription that's scheduled to expire at the end of the current calendar month.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeliverabilityDashboardOptionsResponse) -> dict:
    out: dict = {}
    out["DashboardEnabled"] = value.get("dashboard_enabled", False)
    if "subscription_expiry_date" in value:
        import capo_pinpoint_email.types.timestamp

        out["SubscriptionExpiryDate"] = (
            capo_pinpoint_email.types.timestamp.serialize_json(
                value["subscription_expiry_date"]
            )
        )
    if "account_status" in value:
        import capo_pinpoint_email.types.deliverability_dashboard_account_status

        out["AccountStatus"] = (
            capo_pinpoint_email.types.deliverability_dashboard_account_status.serialize_json(
                value["account_status"]
            )
        )
    if "active_subscribed_domains" in value:
        import capo_pinpoint_email.types.domain_deliverability_tracking_options

        out["ActiveSubscribedDomains"] = (
            capo_pinpoint_email.types.domain_deliverability_tracking_options.serialize_json(
                value["active_subscribed_domains"]
            )
        )
    if "pending_expiration_subscribed_domains" in value:
        import capo_pinpoint_email.types.domain_deliverability_tracking_options

        out["PendingExpirationSubscribedDomains"] = (
            capo_pinpoint_email.types.domain_deliverability_tracking_options.serialize_json(
                value["pending_expiration_subscribed_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDeliverabilityDashboardOptionsResponse:
    out: GetDeliverabilityDashboardOptionsResponse = {}  # type: ignore[typeddict-item]
    if "DashboardEnabled" in data:
        out["dashboard_enabled"] = data["DashboardEnabled"]
    else:
        out["dashboard_enabled"] = False
    if "SubscriptionExpiryDate" in data:
        import capo_pinpoint_email.types.timestamp

        out["subscription_expiry_date"] = (
            capo_pinpoint_email.types.timestamp.deserialize_json(
                data["SubscriptionExpiryDate"]
            )
        )
    if "AccountStatus" in data:
        import capo_pinpoint_email.types.deliverability_dashboard_account_status

        out["account_status"] = (
            capo_pinpoint_email.types.deliverability_dashboard_account_status.deserialize_json(
                data["AccountStatus"]
            )
        )
    if "ActiveSubscribedDomains" in data:
        import capo_pinpoint_email.types.domain_deliverability_tracking_options

        out["active_subscribed_domains"] = (
            capo_pinpoint_email.types.domain_deliverability_tracking_options.deserialize_json(
                data["ActiveSubscribedDomains"]
            )
        )
    if "PendingExpirationSubscribedDomains" in data:
        import capo_pinpoint_email.types.domain_deliverability_tracking_options

        out["pending_expiration_subscribed_domains"] = (
            capo_pinpoint_email.types.domain_deliverability_tracking_options.deserialize_json(
                data["PendingExpirationSubscribedDomains"]
            )
        )
    return out
