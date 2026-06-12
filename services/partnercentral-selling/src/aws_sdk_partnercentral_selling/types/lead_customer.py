"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadCustomer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.address_summary
    import aws_sdk_partnercentral_selling.types.aws_maturity
    import aws_sdk_partnercentral_selling.types.company_name
    import aws_sdk_partnercentral_selling.types.company_website_url
    import aws_sdk_partnercentral_selling.types.industry
    import aws_sdk_partnercentral_selling.types.market_segment


class LeadCustomer(TypedDict):
    industry: NotRequired["aws_sdk_partnercentral_selling.types.industry.Industry"]
    """<p>Specifies the industry sector to which the lead customer's company belongs. This categorization helps in understanding the customer's business context and tailoring appropriate solutions.</p>"""
    company_name: "aws_sdk_partnercentral_selling.types.company_name.CompanyName"
    """<p>The name of the lead customer's company. This field is essential for identifying and tracking the customer organization associated with the lead.</p>"""
    website_url: NotRequired[
        "aws_sdk_partnercentral_selling.types.company_website_url.CompanyWebsiteUrl"
    ]
    """<p>The website URL of the lead customer's company. This provides additional context about the customer organization and helps verify company legitimacy and size.</p>"""
    address: "aws_sdk_partnercentral_selling.types.address_summary.AddressSummary"
    aws_maturity: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_maturity.AwsMaturity"
    ]
    """<p>Indicates the customer's level of experience and adoption with AWS services. This assessment helps determine the appropriate engagement approach and solution complexity.</p>"""
    market_segment: NotRequired[
        "aws_sdk_partnercentral_selling.types.market_segment.MarketSegment"
    ]
    """<p>Specifies the market segment classification of the lead customer, such as enterprise, mid-market, or small business. This segmentation helps in targeting appropriate solutions and engagement strategies.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadCustomer) -> dict:
    out: dict = {}
    if "industry" in value:
        import aws_sdk_partnercentral_selling.types.industry

        out["Industry"] = (
            aws_sdk_partnercentral_selling.types.industry.serialize_aws_json_1_0(
                value["industry"]
            )
        )
    out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    import aws_sdk_partnercentral_selling.types.address_summary

    out["Address"] = (
        aws_sdk_partnercentral_selling.types.address_summary.serialize_aws_json_1_0(
            value["address"]
        )
    )
    if "aws_maturity" in value:
        out["AwsMaturity"] = value["aws_maturity"]
    if "market_segment" in value:
        import aws_sdk_partnercentral_selling.types.market_segment

        out["MarketSegment"] = (
            aws_sdk_partnercentral_selling.types.market_segment.serialize_aws_json_1_0(
                value["market_segment"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadCustomer:
    out: LeadCustomer = {}  # type: ignore[typeddict-item]
    if "Industry" in data:
        import aws_sdk_partnercentral_selling.types.industry

        out["industry"] = (
            aws_sdk_partnercentral_selling.types.industry.deserialize_aws_json_1_0(
                data["Industry"]
            )
        )
    if "CompanyName" in data:
        out["company_name"] = data["CompanyName"]
    else:
        raise DeserializationError("LeadCustomer.company_name required")
    if "WebsiteUrl" in data:
        out["website_url"] = data["WebsiteUrl"]
    if "Address" in data:
        import aws_sdk_partnercentral_selling.types.address_summary

        out["address"] = (
            aws_sdk_partnercentral_selling.types.address_summary.deserialize_aws_json_1_0(
                data["Address"]
            )
        )
    else:
        raise DeserializationError("LeadCustomer.address required")
    if "AwsMaturity" in data:
        out["aws_maturity"] = data["AwsMaturity"]
    if "MarketSegment" in data:
        import aws_sdk_partnercentral_selling.types.market_segment

        out["market_segment"] = (
            aws_sdk_partnercentral_selling.types.market_segment.deserialize_aws_json_1_0(
                data["MarketSegment"]
            )
        )
    return out
