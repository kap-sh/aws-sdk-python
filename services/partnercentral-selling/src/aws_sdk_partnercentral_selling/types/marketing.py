"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Marketing``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_funding_used
    import aws_sdk_partnercentral_selling.types.channels
    import aws_sdk_partnercentral_selling.types.marketing_source
    import aws_sdk_partnercentral_selling.types.use_cases


class Marketing(TypedDict):
    campaign_name: NotRequired["str"]
    """<p>Specifies the <code>Opportunity</code> marketing campaign code. The Amazon Web Services campaign code is a reference to specific marketing initiatives, promotions, or activities. This field captures the identifier used to track and categorize the <code>Opportunity</code> within marketing campaigns. If you don't have a campaign code, contact your Amazon Web Services point of contact to obtain one.</p>"""
    source: NotRequired[
        "aws_sdk_partnercentral_selling.types.marketing_source.MarketingSource"
    ]
    """<p>Indicates if the <code>Opportunity</code> was sourced from an Amazon Web Services marketing activity. Use the value <code>Marketing Activity</code>. Use <code>None</code> if it's not associated with an Amazon Web Services marketing activity. This field helps Amazon Web Services track the return on marketing investments and enables better distribution of marketing budgets among partners.</p>"""
    use_cases: NotRequired["aws_sdk_partnercentral_selling.types.use_cases.UseCases"]
    """<p>Specifies the marketing activity use case or purpose that led to the <code>Opportunity</code>'s creation or contact. This field captures the context or marketing activity's execution's intention and the direct correlation to the generated opportunity or contact. Must be empty when <code>Marketing.AWSFundingUsed = No</code>.</p> <p>Valid values: <code>AI/ML | Analytics | Application Integration | Blockchain | Business Applications | Cloud Financial Management | Compute | Containers | Customer Engagement | Databases | Developer Tools | End User Computing | Front End Web &amp; Mobile | Game Tech | IoT | Management &amp; Governance | Media Services | Migration &amp; Transfer | Networking &amp; Content Delivery | Quantum Technologies | Robotics | Satellite | Security | Serverless | Storage | VR &amp; AR</code> </p>"""
    channels: NotRequired["aws_sdk_partnercentral_selling.types.channels.Channels"]
    """<p>Specifies the <code>Opportunity</code>'s channel that the marketing activity is associated with or was contacted through. This field provides information about the specific marketing channel that contributed to the generation of the lead or contact.</p>"""
    aws_funding_used: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_funding_used.AwsFundingUsed"
    ]
    """<p>Indicates if the <code>Opportunity</code> is a marketing development fund (MDF) funded activity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Marketing) -> dict:
    out: dict = {}
    if "campaign_name" in value:
        out["CampaignName"] = value["campaign_name"]
    if "source" in value:
        import aws_sdk_partnercentral_selling.types.marketing_source

        out["Source"] = (
            aws_sdk_partnercentral_selling.types.marketing_source.serialize_aws_json_1_0(
                value["source"]
            )
        )
    if "use_cases" in value:
        import aws_sdk_partnercentral_selling.types.use_cases

        out["UseCases"] = (
            aws_sdk_partnercentral_selling.types.use_cases.serialize_aws_json_1_0(
                value["use_cases"]
            )
        )
    if "channels" in value:
        import aws_sdk_partnercentral_selling.types.channels

        out["Channels"] = (
            aws_sdk_partnercentral_selling.types.channels.serialize_aws_json_1_0(
                value["channels"]
            )
        )
    if "aws_funding_used" in value:
        import aws_sdk_partnercentral_selling.types.aws_funding_used

        out["AwsFundingUsed"] = (
            aws_sdk_partnercentral_selling.types.aws_funding_used.serialize_aws_json_1_0(
                value["aws_funding_used"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Marketing:
    out: Marketing = {}  # type: ignore[typeddict-item]
    if "CampaignName" in data:
        out["campaign_name"] = data["CampaignName"]
    if "Source" in data:
        import aws_sdk_partnercentral_selling.types.marketing_source

        out["source"] = (
            aws_sdk_partnercentral_selling.types.marketing_source.deserialize_aws_json_1_0(
                data["Source"]
            )
        )
    if "UseCases" in data:
        import aws_sdk_partnercentral_selling.types.use_cases

        out["use_cases"] = (
            aws_sdk_partnercentral_selling.types.use_cases.deserialize_aws_json_1_0(
                data["UseCases"]
            )
        )
    if "Channels" in data:
        import aws_sdk_partnercentral_selling.types.channels

        out["channels"] = (
            aws_sdk_partnercentral_selling.types.channels.deserialize_aws_json_1_0(
                data["Channels"]
            )
        )
    if "AwsFundingUsed" in data:
        import aws_sdk_partnercentral_selling.types.aws_funding_used

        out["aws_funding_used"] = (
            aws_sdk_partnercentral_selling.types.aws_funding_used.deserialize_aws_json_1_0(
                data["AwsFundingUsed"]
            )
        )
    return out
