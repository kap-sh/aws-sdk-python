"""Generated from Smithy shape ``com.amazonaws.pinpointemail#GetDomainDeliverabilityCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.campaign_id


class GetDomainDeliverabilityCampaignRequest(TypedDict, closed=True):
    campaign_id: "capo_pinpoint_email.types.campaign_id.CampaignId"
    """<p>The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns this identifier to a campaign. This value is not the same as the campaign identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint API or the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainDeliverabilityCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainDeliverabilityCampaignRequest:
    out: GetDomainDeliverabilityCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
