"""Generated from Smithy shape ``com.amazonaws.sesv2#ListDomainDeliverabilityCampaignsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.domain
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token
    import aws_sdk_sesv2.types.timestamp


class ListDomainDeliverabilityCampaignsRequest(TypedDict):
    start_date: "aws_sdk_sesv2.types.timestamp.Timestamp"
    """<p>The first day that you want to obtain deliverability data for.</p>"""
    end_date: "aws_sdk_sesv2.types.timestamp.Timestamp"
    """<p>The last day that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the <code>StartDate</code> parameter.</p>"""
    subscribed_domain: "aws_sdk_sesv2.types.domain.Domain"
    """<p>The domain to obtain deliverability data for.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token that’s returned from a previous call to the <code>ListDomainDeliverabilityCampaigns</code> operation. This token indicates the position of a campaign in the list of campaigns.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>The maximum number of results to include in response to a single call to the <code>ListDomainDeliverabilityCampaigns</code> operation. If the number of results is larger than the number that you specify in this parameter, the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainDeliverabilityCampaignsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainDeliverabilityCampaignsRequest:
    out: ListDomainDeliverabilityCampaignsRequest = {}  # type: ignore[typeddict-item]
    return out
