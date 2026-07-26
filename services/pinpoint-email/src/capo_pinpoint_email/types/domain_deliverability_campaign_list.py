"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DomainDeliverabilityCampaignList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint_email.types.domain_deliverability_campaign

DomainDeliverabilityCampaignList: TypeAlias = list[
    "capo_pinpoint_email.types.domain_deliverability_campaign.DomainDeliverabilityCampaign"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainDeliverabilityCampaignList) -> list:
    import capo_pinpoint_email.types.domain_deliverability_campaign

    out: list = []
    for item in value:
        out.append(
            capo_pinpoint_email.types.domain_deliverability_campaign.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DomainDeliverabilityCampaignList:
    import capo_pinpoint_email.types.domain_deliverability_campaign

    out: DomainDeliverabilityCampaignList = []
    for item in data:
        out.append(
            capo_pinpoint_email.types.domain_deliverability_campaign.deserialize_json(
                item
            )
        )
    return out
