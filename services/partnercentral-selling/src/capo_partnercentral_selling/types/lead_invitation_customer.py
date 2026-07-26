"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInvitationCustomer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_maturity
    import capo_partnercentral_selling.types.company_name
    import capo_partnercentral_selling.types.company_website_url
    import capo_partnercentral_selling.types.country_code
    import capo_partnercentral_selling.types.industry
    import capo_partnercentral_selling.types.market_segment


class LeadInvitationCustomer(TypedDict, closed=True):
    industry: NotRequired["capo_partnercentral_selling.types.industry.Industry"]
    """<p>Specifies the industry sector of the customer company associated with the lead invitation. This categorization helps partners understand the customer's business context and assess solution fit.</p>"""
    company_name: "capo_partnercentral_selling.types.company_name.CompanyName"
    """<p>The name of the customer company associated with the lead invitation. This field identifies the target organization for the lead engagement opportunity.</p>"""
    website_url: NotRequired[
        "capo_partnercentral_selling.types.company_website_url.CompanyWebsiteUrl"
    ]
    """<p>The website URL of the customer company. This provides additional context about the customer organization and helps partners verify company details and assess business size and legitimacy.</p>"""
    country_code: "capo_partnercentral_selling.types.country_code.CountryCode"
    """<p>The country code indicating the geographic location of the customer company. This information helps partners understand regional requirements and assess their ability to serve the customer effectively.</p>"""
    aws_maturity: NotRequired[
        "capo_partnercentral_selling.types.aws_maturity.AwsMaturity"
    ]
    """<p>Indicates the customer's level of experience and adoption with AWS services. This assessment helps partners understand the customer's cloud maturity and tailor their engagement approach accordingly.</p>"""
    market_segment: NotRequired[
        "capo_partnercentral_selling.types.market_segment.MarketSegment"
    ]
    """<p>Specifies the market segment classification of the customer, such as enterprise, mid-market, or small business. This segmentation helps partners determine the appropriate solution complexity and engagement strategy.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInvitationCustomer) -> dict:
    out: dict = {}
    if "industry" in value:
        import capo_partnercentral_selling.types.industry

        out["Industry"] = (
            capo_partnercentral_selling.types.industry.serialize_aws_json_1_0(
                value["industry"]
            )
        )
    out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    import capo_partnercentral_selling.types.country_code

    out["CountryCode"] = (
        capo_partnercentral_selling.types.country_code.serialize_aws_json_1_0(
            value["country_code"]
        )
    )
    if "aws_maturity" in value:
        out["AwsMaturity"] = value["aws_maturity"]
    if "market_segment" in value:
        import capo_partnercentral_selling.types.market_segment

        out["MarketSegment"] = (
            capo_partnercentral_selling.types.market_segment.serialize_aws_json_1_0(
                value["market_segment"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadInvitationCustomer:
    out: LeadInvitationCustomer = {}  # type: ignore[typeddict-item]
    if "Industry" in data:
        import capo_partnercentral_selling.types.industry

        out["industry"] = (
            capo_partnercentral_selling.types.industry.deserialize_aws_json_1_0(
                data["Industry"]
            )
        )
    if "CompanyName" in data:
        out["company_name"] = data["CompanyName"]
    else:
        raise DeserializationError("LeadInvitationCustomer.company_name required")
    if "WebsiteUrl" in data:
        out["website_url"] = data["WebsiteUrl"]
    if "CountryCode" in data:
        import capo_partnercentral_selling.types.country_code

        out["country_code"] = (
            capo_partnercentral_selling.types.country_code.deserialize_aws_json_1_0(
                data["CountryCode"]
            )
        )
    else:
        raise DeserializationError("LeadInvitationCustomer.country_code required")
    if "AwsMaturity" in data:
        out["aws_maturity"] = data["AwsMaturity"]
    if "MarketSegment" in data:
        import capo_partnercentral_selling.types.market_segment

        out["market_segment"] = (
            capo_partnercentral_selling.types.market_segment.deserialize_aws_json_1_0(
                data["MarketSegment"]
            )
        )
    return out
