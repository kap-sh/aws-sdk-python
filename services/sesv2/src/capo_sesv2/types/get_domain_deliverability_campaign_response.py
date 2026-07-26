"""Generated from Smithy shape ``com.amazonaws.sesv2#GetDomainDeliverabilityCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.domain_deliverability_campaign


class GetDomainDeliverabilityCampaignResponse(TypedDict, closed=True):
    domain_deliverability_campaign: (
        "capo_sesv2.types.domain_deliverability_campaign.DomainDeliverabilityCampaign"
    )
    """<p>An object that contains the deliverability data for the campaign.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainDeliverabilityCampaignResponse) -> dict:
    out: dict = {}
    import capo_sesv2.types.domain_deliverability_campaign

    out["DomainDeliverabilityCampaign"] = (
        capo_sesv2.types.domain_deliverability_campaign.serialize_json(
            value["domain_deliverability_campaign"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDomainDeliverabilityCampaignResponse:
    out: GetDomainDeliverabilityCampaignResponse = {}  # type: ignore[typeddict-item]
    if "DomainDeliverabilityCampaign" in data:
        import capo_sesv2.types.domain_deliverability_campaign

        out["domain_deliverability_campaign"] = (
            capo_sesv2.types.domain_deliverability_campaign.deserialize_json(
                data["DomainDeliverabilityCampaign"]
            )
        )
    else:
        raise DeserializationError(
            "GetDomainDeliverabilityCampaignResponse.domain_deliverability_campaign required"
        )
    return out
