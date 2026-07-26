"""Generated from Smithy shape ``com.amazonaws.personalize#CampaignSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.date
    import capo_personalize.types.failure_reason
    import capo_personalize.types.name
    import capo_personalize.types.status


class CampaignSummary(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the campaign.</p>"""
    campaign_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the campaign.</p>"""
    status: NotRequired["capo_personalize.types.status.Status"]
    """<p>The status of the campaign.</p> <p>A campaign can be in one of the following states:</p> <ul> <li> <p>CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED</p> </li> <li> <p>DELETE PENDING > DELETE IN_PROGRESS</p> </li> </ul>"""
    creation_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the campaign was created.</p>"""
    last_updated_date_time: NotRequired["capo_personalize.types.date.Date"]
    """<p>The date and time (in Unix time) that the campaign was last updated.</p>"""
    failure_reason: NotRequired["capo_personalize.types.failure_reason.FailureReason"]
    """<p>If a campaign fails, the reason behind the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CampaignSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "campaign_arn" in value:
        out["campaignArn"] = value["campaign_arn"]
    if "status" in value:
        out["status"] = value["status"]
    if "creation_date_time" in value:
        import capo_personalize.types.date

        out["creationDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["creation_date_time"]
        )
    if "last_updated_date_time" in value:
        import capo_personalize.types.date

        out["lastUpdatedDateTime"] = capo_personalize.types.date.serialize_aws_json_1_1(
            value["last_updated_date_time"]
        )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CampaignSummary:
    out: CampaignSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "campaignArn" in data:
        out["campaign_arn"] = data["campaignArn"]
    if "status" in data:
        out["status"] = data["status"]
    if "creationDateTime" in data:
        import capo_personalize.types.date

        out["creation_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["creationDateTime"]
            )
        )
    if "lastUpdatedDateTime" in data:
        import capo_personalize.types.date

        out["last_updated_date_time"] = (
            capo_personalize.types.date.deserialize_aws_json_1_1(
                data["lastUpdatedDateTime"]
            )
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
