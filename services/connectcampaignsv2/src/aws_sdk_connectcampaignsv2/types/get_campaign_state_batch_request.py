"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#GetCampaignStateBatchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id_list


class GetCampaignStateBatchRequest(TypedDict):
    campaign_ids: "aws_sdk_connectcampaignsv2.types.campaign_id_list.CampaignIdList"


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignStateBatchRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.campaign_id_list

    out["campaignIds"] = (
        aws_sdk_connectcampaignsv2.types.campaign_id_list.serialize_json(
            value["campaign_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetCampaignStateBatchRequest:
    out: GetCampaignStateBatchRequest = {}  # type: ignore[typeddict-item]
    if "campaignIds" in data:
        import aws_sdk_connectcampaignsv2.types.campaign_id_list

        out["campaign_ids"] = (
            aws_sdk_connectcampaignsv2.types.campaign_id_list.deserialize_json(
                data["campaignIds"]
            )
        )
    else:
        raise DeserializationError("GetCampaignStateBatchRequest.campaign_ids required")
    return out
