"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DomainDeliverabilityTrackingOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.domain_deliverability_tracking_option

DomainDeliverabilityTrackingOptions: TypeAlias = list[
    "capo_pinpoint_email.types.domain_deliverability_tracking_option.DomainDeliverabilityTrackingOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainDeliverabilityTrackingOptions) -> list:
    import capo_pinpoint_email.types.domain_deliverability_tracking_option

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_email.types.domain_deliverability_tracking_option.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DomainDeliverabilityTrackingOptions:
    import capo_pinpoint_email.types.domain_deliverability_tracking_option

    out: DomainDeliverabilityTrackingOptions = []
    for item in data:
        out.append(
            capo_pinpoint_email.types.domain_deliverability_tracking_option.deserialize_json(
                item
            )
        )
    return out
