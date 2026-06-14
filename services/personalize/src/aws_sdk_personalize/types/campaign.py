"""Generated from Smithy shape ``com.amazonaws.personalize#Campaign``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.campaign_config
    import aws_sdk_personalize.types.campaign_update_summary
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.name
    import aws_sdk_personalize.types.status
    import aws_sdk_personalize.types.transactions_per_second


class Campaign(TypedDict):
    name: NotRequired["aws_sdk_personalize.types.name.Name"]
    """<p>The name of the campaign.</p>"""
    campaign_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the campaign. </p>"""
    solution_version_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the solution version the campaign uses.</p>"""
    min_provisioned_tps: NotRequired[
        "aws_sdk_personalize.types.transactions_per_second.TransactionsPerSecond"
    ]
    """<p>Specifies the requested minimum provisioned transactions (recommendations) per second. A high <code>minProvisionedTPS</code> will increase your bill. We recommend starting with 1 for <code>minProvisionedTPS</code> (the default). Track your usage using Amazon CloudWatch metrics, and increase the <code>minProvisionedTPS</code> as necessary.</p>"""
    campaign_config: NotRequired[
        "aws_sdk_personalize.types.campaign_config.CampaignConfig"
    ]
    """<p>The configuration details of a campaign.</p>"""
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the campaign.</p> <p>A campaign can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If a campaign fails, the reason behind the failure.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the campaign was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix format) that the campaign was last updated.</p>"""
    latest_campaign_update: NotRequired[
        "aws_sdk_personalize.types.campaign_update_summary.CampaignUpdateSummary"
    ]
    r"""<p>Provides a summary of the properties of a campaign update. For a complete listing, call the <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeCampaign.html\">DescribeCampaign</a> API.</p> <note> <p>The <code>latestCampaignUpdate</code> field is only returned when the campaign has had at least one <code>UpdateCampaign</code> call. </p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Campaign) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "campaign_arn" in value:
        out["campaignArn"] = value["campaign_arn"]
    if "solution_version_arn" in value:
        out["solutionVersionArn"] = value["solution_version_arn"]
    if "min_provisioned_tps" in value:
        out["minProvisionedTPS"] = value["min_provisioned_tps"]
    if "campaign_config" in value:
        import aws_sdk_personalize.types.campaign_config

        out["campaignConfig"] = (
            aws_sdk_personalize.types.campaign_config.serialize_aws_json_1_1(
                value["campaign_config"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    if "creation_date_time" in value:
        import aws_sdk_personalize.types.date

        out["creationDateTime"] = aws_sdk_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import aws_sdk_personalize.types.date

        out["lastUpdatedDateTime"] = (
            aws_sdk_personalize.types.date.serialize_aws_json_1_1(
                value["last_updated_date_time"]
            )
        )
    if "latest_campaign_update" in value:
        import aws_sdk_personalize.types.campaign_update_summary

        out["latestCampaignUpdate"] = (
            aws_sdk_personalize.types.campaign_update_summary.serialize_aws_json_1_1(
                value["latest_campaign_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Campaign:
    out: Campaign = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "campaignArn" in data:
        out["campaign_arn"] = data["campaignArn"]
    if "solutionVersionArn" in data:
        out["solution_version_arn"] = data["solutionVersionArn"]
    if "minProvisionedTPS" in data:
        out["min_provisioned_tps"] = data["minProvisionedTPS"]
    if "campaignConfig" in data:
        import aws_sdk_personalize.types.campaign_config

        out["campaign_config"] = (
            aws_sdk_personalize.types.campaign_config.deserialize_aws_json_1_1(
                data["campaignConfig"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "creationDateTime" in data:
        import aws_sdk_personalize.types.date

        out["creation_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import aws_sdk_personalize.types.date

        out["last_updated_date_time"] = (
            aws_sdk_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "latestCampaignUpdate" in data:
        import aws_sdk_personalize.types.campaign_update_summary

        out["latest_campaign_update"] = (
            aws_sdk_personalize.types.campaign_update_summary.deserialize_aws_json_1_1(
                data["latestCampaignUpdate"]
            )
        )
    return out
