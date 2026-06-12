"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignFlowAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.arn
    import aws_sdk_connectcampaignsv2.types.campaign_id


class UpdateCampaignFlowAssociationRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    connect_campaign_flow_arn: "aws_sdk_connectcampaignsv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignFlowAssociationRequest) -> dict:
    out: dict = {}
    out["connectCampaignFlowArn"] = value["connect_campaign_flow_arn"]
    return out


def deserialize_json(data: dict) -> UpdateCampaignFlowAssociationRequest:
    out: UpdateCampaignFlowAssociationRequest = {}  # type: ignore[typeddict-item]
    if "connectCampaignFlowArn" in data:
        out["connect_campaign_flow_arn"] = data["connectCampaignFlowArn"]
    else:
        raise DeserializationError(
            "UpdateCampaignFlowAssociationRequest.connect_campaign_flow_arn required"
        )
    return out
