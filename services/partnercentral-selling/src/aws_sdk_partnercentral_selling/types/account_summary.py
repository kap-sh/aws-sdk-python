"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.address_summary
    import aws_sdk_partnercentral_selling.types.industry
    import aws_sdk_partnercentral_selling.types.name
    import aws_sdk_partnercentral_selling.types.website_url


class AccountSummary(TypedDict, closed=True):
    industry: NotRequired["aws_sdk_partnercentral_selling.types.industry.Industry"]
    """<p>Specifies which industry the end <code>Customer</code> belongs to associated with the <code>Opportunity</code>. It refers to the category or sector that the customer's business operates in.</p> <p>To submit a value outside the picklist, use <code>Other</code>.</p> <p>Conditionally mandatory if <code>Other</code> is selected for Industry Vertical in LOVs.</p>"""
    other_industry: NotRequired["str"]
    """<p>Specifies the end <code>Customer</code>'s industry associated with the <code> Opportunity</code>, when the selected value in the <code>Industry</code> field is <code>Other</code>. This field is relevant when the customer's industry doesn't fall under the predefined picklist values and requires a custom description.</p>"""
    company_name: "aws_sdk_partnercentral_selling.types.name.Name"
    """<p>Specifies the end <code>Customer</code>'s company name associated with the <code>Opportunity</code>.</p>"""
    website_url: NotRequired[
        "aws_sdk_partnercentral_selling.types.website_url.WebsiteUrl"
    ]
    """<p>Specifies the end customer's company website URL associated with the <code>Opportunity</code>. This value is crucial to map the customer within the Amazon Web Services CRM system.</p>"""
    address: NotRequired[
        "aws_sdk_partnercentral_selling.types.address_summary.AddressSummary"
    ]
    """<p>Specifies the end <code>Customer</code>'s address details associated with the <code>Opportunity</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountSummary) -> dict:
    out: dict = {}
    if "industry" in value:
        import aws_sdk_partnercentral_selling.types.industry

        out["Industry"] = (
            aws_sdk_partnercentral_selling.types.industry.serialize_aws_json_1_0(
                value["industry"]
            )
        )
    if "other_industry" in value:
        out["OtherIndustry"] = value["other_industry"]
    out["CompanyName"] = value["company_name"]
    if "website_url" in value:
        out["WebsiteUrl"] = value["website_url"]
    if "address" in value:
        import aws_sdk_partnercentral_selling.types.address_summary

        out["Address"] = (
            aws_sdk_partnercentral_selling.types.address_summary.serialize_aws_json_1_0(
                value["address"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountSummary:
    out: AccountSummary = {}  # type: ignore[typeddict-item]
    if "Industry" in data:
        import aws_sdk_partnercentral_selling.types.industry

        out["industry"] = (
            aws_sdk_partnercentral_selling.types.industry.deserialize_aws_json_1_0(
                data["Industry"]
            )
        )
    if "OtherIndustry" in data:
        out["other_industry"] = data["OtherIndustry"]
    if "CompanyName" in data:
        out["company_name"] = data["CompanyName"]
    else:
        raise DeserializationError("AccountSummary.company_name required")
    if "WebsiteUrl" in data:
        out["website_url"] = data["WebsiteUrl"]
    if "Address" in data:
        import aws_sdk_partnercentral_selling.types.address_summary

        out["address"] = (
            aws_sdk_partnercentral_selling.types.address_summary.deserialize_aws_json_1_0(
                data["Address"]
            )
        )
    return out
