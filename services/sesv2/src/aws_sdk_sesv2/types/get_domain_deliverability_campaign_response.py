"""Generated from Smithy shape ``com.amazonaws.sesv2#GetDomainDeliverabilityCampaignResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.domain_deliverability_campaign


class GetDomainDeliverabilityCampaignResponse(TypedDict):
    domain_deliverability_campaign: "aws_sdk_sesv2.types.domain_deliverability_campaign.DomainDeliverabilityCampaign"
    """<p>An object that contains the deliverability data for the campaign.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainDeliverabilityCampaignResponse) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.domain_deliverability_campaign

    out["DomainDeliverabilityCampaign"] = (
        aws_sdk_sesv2.types.domain_deliverability_campaign.serialize_json(
            value["domain_deliverability_campaign"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDomainDeliverabilityCampaignResponse:
    out: GetDomainDeliverabilityCampaignResponse = {}  # type: ignore[typeddict-item]
    if "DomainDeliverabilityCampaign" in data:
        import aws_sdk_sesv2.types.domain_deliverability_campaign

        out["domain_deliverability_campaign"] = (
            aws_sdk_sesv2.types.domain_deliverability_campaign.deserialize_json(
                data["DomainDeliverabilityCampaign"]
            )
        )
    else:
        raise DeserializationError(
            "GetDomainDeliverabilityCampaignResponse.domain_deliverability_campaign required"
        )
    return out
