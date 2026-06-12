"""Generated from Smithy shape ``com.amazonaws.sesv2#GetDomainDeliverabilityCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.campaign_id


class GetDomainDeliverabilityCampaignRequest(TypedDict):
    campaign_id: "aws_sdk_sesv2.types.campaign_id.CampaignId"
    """<p>The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainDeliverabilityCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainDeliverabilityCampaignRequest:
    out: GetDomainDeliverabilityCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
