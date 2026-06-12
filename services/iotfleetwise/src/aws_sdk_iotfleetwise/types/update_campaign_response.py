"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateCampaignResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.campaign_arn
    import aws_sdk_iotfleetwise.types.campaign_name
    import aws_sdk_iotfleetwise.types.campaign_status


class UpdateCampaignResponse(TypedDict):
    arn: NotRequired["aws_sdk_iotfleetwise.types.campaign_arn.campaignArn"]
    """<p> The Amazon Resource Name (ARN) of the campaign. </p>"""
    name: NotRequired["aws_sdk_iotfleetwise.types.campaign_name.campaignName"]
    """<p>The name of the updated campaign.</p>"""
    status: NotRequired["aws_sdk_iotfleetwise.types.campaign_status.CampaignStatus"]
    """<p>The state of a campaign. The status can be one of:</p> <ul> <li> <p> <code>CREATING</code> - Amazon Web Services IoT FleetWise is processing your request to create the campaign. </p> </li> <li> <p> <code>WAITING_FOR_APPROVAL</code> - After you create a campaign, it enters this state. Use the API operation to approve the campaign for deployment to the target vehicle or fleet. </p> </li> <li> <p> <code>RUNNING</code> - The campaign is active. </p> </li> <li> <p> <code>SUSPENDED</code> - The campaign is suspended. To resume the campaign, use the API operation. </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCampaignResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import aws_sdk_iotfleetwise.types.campaign_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.campaign_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCampaignResponse:
    out: UpdateCampaignResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_iotfleetwise.types.campaign_status

        out["status"] = (
            aws_sdk_iotfleetwise.types.campaign_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
