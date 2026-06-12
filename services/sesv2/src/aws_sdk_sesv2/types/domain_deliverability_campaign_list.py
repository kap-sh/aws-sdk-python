"""Generated from Smithy shape ``com.amazonaws.sesv2#DomainDeliverabilityCampaignList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.domain_deliverability_campaign

DomainDeliverabilityCampaignList: TypeAlias = list[
    "aws_sdk_sesv2.types.domain_deliverability_campaign.DomainDeliverabilityCampaign"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainDeliverabilityCampaignList) -> list:
    import aws_sdk_sesv2.types.domain_deliverability_campaign

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sesv2.types.domain_deliverability_campaign.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DomainDeliverabilityCampaignList:
    import aws_sdk_sesv2.types.domain_deliverability_campaign

    out: DomainDeliverabilityCampaignList = []
    for item in data:
        out.append(
            aws_sdk_sesv2.types.domain_deliverability_campaign.deserialize_json(item)
        )
    return out
