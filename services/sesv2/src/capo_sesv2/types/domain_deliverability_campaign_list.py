"""Generated from Smithy shape ``com.amazonaws.sesv2#DomainDeliverabilityCampaignList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.domain_deliverability_campaign

DomainDeliverabilityCampaignList: TypeAlias = list[
    "capo_sesv2.types.domain_deliverability_campaign.DomainDeliverabilityCampaign"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainDeliverabilityCampaignList) -> list:
    import capo_sesv2.types.domain_deliverability_campaign

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.domain_deliverability_campaign.serialize_json(item))
    return out


def deserialize_json(data: list) -> DomainDeliverabilityCampaignList:
    import capo_sesv2.types.domain_deliverability_campaign

    out: DomainDeliverabilityCampaignList = []
    for item in data:
        out.append(
            capo_sesv2.types.domain_deliverability_campaign.deserialize_json(item)
        )
    return out
