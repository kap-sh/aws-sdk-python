"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CreateCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_arn
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.tag_map


class CreateCampaignResponse(TypedDict, closed=True):
    id: NotRequired["capo_connectcampaignsv2.types.campaign_id.CampaignId"]
    arn: NotRequired["capo_connectcampaignsv2.types.campaign_arn.CampaignArn"]
    tags: NotRequired["capo_connectcampaignsv2.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateCampaignResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_connectcampaignsv2.types.tag_map

        out["tags"] = capo_connectcampaignsv2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCampaignResponse:
    out: CreateCampaignResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import capo_connectcampaignsv2.types.tag_map

        out["tags"] = capo_connectcampaignsv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
