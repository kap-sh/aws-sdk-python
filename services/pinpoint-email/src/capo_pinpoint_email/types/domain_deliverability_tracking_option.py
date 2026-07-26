"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DomainDeliverabilityTrackingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.domain
    import capo_pinpoint_email.types.inbox_placement_tracking_option
    import capo_pinpoint_email.types.timestamp


class DomainDeliverabilityTrackingOption(TypedDict, closed=True):
    domain: NotRequired["capo_pinpoint_email.types.domain.Domain"]
    """<p>A verified domain that’s associated with your AWS account and currently has an active Deliverability dashboard subscription.</p>"""
    subscription_start_date: NotRequired[
        "capo_pinpoint_email.types.timestamp.Timestamp"
    ]
    """<p>The date, in Unix time format, when you enabled the Deliverability dashboard for the domain.</p>"""
    inbox_placement_tracking_option: NotRequired[
        "capo_pinpoint_email.types.inbox_placement_tracking_option.InboxPlacementTrackingOption"
    ]
    """<p>An object that contains information about the inbox placement data settings for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainDeliverabilityTrackingOption) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "subscription_start_date" in value:
        import capo_pinpoint_email.types.timestamp

        out["SubscriptionStartDate"] = (
            capo_pinpoint_email.types.timestamp.serialize_json(
                value["subscription_start_date"]
            )
        )
    if "inbox_placement_tracking_option" in value:
        import capo_pinpoint_email.types.inbox_placement_tracking_option

        out["InboxPlacementTrackingOption"] = (
            capo_pinpoint_email.types.inbox_placement_tracking_option.serialize_json(
                value["inbox_placement_tracking_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainDeliverabilityTrackingOption:
    out: DomainDeliverabilityTrackingOption = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "SubscriptionStartDate" in data:
        import capo_pinpoint_email.types.timestamp

        out["subscription_start_date"] = (
            capo_pinpoint_email.types.timestamp.deserialize_json(
                data["SubscriptionStartDate"]
            )
        )
    if "InboxPlacementTrackingOption" in data:
        import capo_pinpoint_email.types.inbox_placement_tracking_option

        out["inbox_placement_tracking_option"] = (
            capo_pinpoint_email.types.inbox_placement_tracking_option.deserialize_json(
                data["InboxPlacementTrackingOption"]
            )
        )
    return out
