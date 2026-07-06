"""Generated from Smithy shape ``com.amazonaws.personalize#CampaignUpdateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn
    import aws_sdk_personalize.types.campaign_config
    import aws_sdk_personalize.types.date
    import aws_sdk_personalize.types.failure_reason
    import aws_sdk_personalize.types.status
    import aws_sdk_personalize.types.transactions_per_second


class CampaignUpdateSummary(TypedDict, closed=True):
    solution_version_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the deployed solution version.</p>"""
    min_provisioned_tps: NotRequired[
        "aws_sdk_personalize.types.transactions_per_second.TransactionsPerSecond"
    ]
    """<p>Specifies the requested minimum provisioned transactions (recommendations) per second that Amazon Personalize will support.</p>"""
    campaign_config: NotRequired[
        "aws_sdk_personalize.types.campaign_config.CampaignConfig"
    ]
    status: NotRequired["aws_sdk_personalize.types.status.Status"]
    """<p>The status of the campaign update.</p> <p>A campaign update can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    failure_reason: NotRequired[
        "aws_sdk_personalize.types.failure_reason.FailureReason"
    ]
    """<p>If a campaign update fails, the reason behind the failure.</p>"""
    creation_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the campaign update was created.</p>"""
    last_updated_date_time: NotRequired["aws_sdk_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the campaign update was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CampaignUpdateSummary) -> dict:
    out: dict = {}
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
    return out


def deserialize_aws_json_1_1(data: dict) -> CampaignUpdateSummary:
    out: CampaignUpdateSummary = {}  # type: ignore[typeddict-item]
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
    return out
