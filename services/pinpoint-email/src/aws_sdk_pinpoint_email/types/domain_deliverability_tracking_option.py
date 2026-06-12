"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DomainDeliverabilityTrackingOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.domain
    import aws_sdk_pinpoint_email.types.inbox_placement_tracking_option
    import aws_sdk_pinpoint_email.types.timestamp


class DomainDeliverabilityTrackingOption(TypedDict):
    domain: NotRequired["aws_sdk_pinpoint_email.types.domain.Domain"]
    """<p>A verified domain that’s associated with your AWS account and currently has an active Deliverability dashboard subscription.</p>"""
    subscription_start_date: NotRequired[
        "aws_sdk_pinpoint_email.types.timestamp.Timestamp"
    ]
    """<p>The date, in Unix time format, when you enabled the Deliverability dashboard for the domain.</p>"""
    inbox_placement_tracking_option: NotRequired[
        "aws_sdk_pinpoint_email.types.inbox_placement_tracking_option.InboxPlacementTrackingOption"
    ]
    """<p>An object that contains information about the inbox placement data settings for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainDeliverabilityTrackingOption) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "subscription_start_date" in value:
        import aws_sdk_pinpoint_email.types.timestamp

        out["SubscriptionStartDate"] = (
            aws_sdk_pinpoint_email.types.timestamp.serialize_json(
                value["subscription_start_date"]
            )
        )
    if "inbox_placement_tracking_option" in value:
        import aws_sdk_pinpoint_email.types.inbox_placement_tracking_option

        out["InboxPlacementTrackingOption"] = (
            aws_sdk_pinpoint_email.types.inbox_placement_tracking_option.serialize_json(
                value["inbox_placement_tracking_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> DomainDeliverabilityTrackingOption:
    out: DomainDeliverabilityTrackingOption = {}  # type: ignore[typeddict-item]
    if "Domain" in data:
        out["domain"] = data["Domain"]
    if "SubscriptionStartDate" in data:
        import aws_sdk_pinpoint_email.types.timestamp

        out["subscription_start_date"] = (
            aws_sdk_pinpoint_email.types.timestamp.deserialize_json(
                data["SubscriptionStartDate"]
            )
        )
    if "InboxPlacementTrackingOption" in data:
        import aws_sdk_pinpoint_email.types.inbox_placement_tracking_option

        out["inbox_placement_tracking_option"] = (
            aws_sdk_pinpoint_email.types.inbox_placement_tracking_option.deserialize_json(
                data["InboxPlacementTrackingOption"]
            )
        )
    return out
