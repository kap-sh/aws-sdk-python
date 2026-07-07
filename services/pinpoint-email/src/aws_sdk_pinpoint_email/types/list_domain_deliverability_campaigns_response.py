"""Generated from Smithy shape ``com.amazonaws.pinpointemail#ListDomainDeliverabilityCampaignsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.domain_deliverability_campaign_list
    import aws_sdk_pinpoint_email.types.next_token


class ListDomainDeliverabilityCampaignsResponse(TypedDict, closed=True):
    domain_deliverability_campaigns: "aws_sdk_pinpoint_email.types.domain_deliverability_campaign_list.DomainDeliverabilityCampaignList"
    """<p>An array of responses, one for each campaign that used the domain to send email during the specified time range.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint_email.types.next_token.NextToken"]
    """<p>A token that’s returned from a previous call to the <code>ListDomainDeliverabilityCampaigns</code> operation. This token indicates the position of the campaign in the list of campaigns.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainDeliverabilityCampaignsResponse) -> dict:
    out: dict = {}
    import aws_sdk_pinpoint_email.types.domain_deliverability_campaign_list

    out["DomainDeliverabilityCampaigns"] = (
        aws_sdk_pinpoint_email.types.domain_deliverability_campaign_list.serialize_json(
            value["domain_deliverability_campaigns"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainDeliverabilityCampaignsResponse:
    out: ListDomainDeliverabilityCampaignsResponse = {}  # type: ignore[typeddict-item]
    if "DomainDeliverabilityCampaigns" in data:
        import aws_sdk_pinpoint_email.types.domain_deliverability_campaign_list

        out["domain_deliverability_campaigns"] = (
            aws_sdk_pinpoint_email.types.domain_deliverability_campaign_list.deserialize_json(
                data["DomainDeliverabilityCampaigns"]
            )
        )
    else:
        raise DeserializationError(
            "ListDomainDeliverabilityCampaignsResponse.domain_deliverability_campaigns required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
