"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#CreateCampaignResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_arn
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.tag_map


class CreateCampaignResponse(TypedDict):
    id: NotRequired["aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"]
    arn: NotRequired["aws_sdk_connectcampaignsv2.types.campaign_arn.CampaignArn"]
    tags: NotRequired["aws_sdk_connectcampaignsv2.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateCampaignResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_connectcampaignsv2.types.tag_map

        out["tags"] = aws_sdk_connectcampaignsv2.types.tag_map.serialize_json(
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
        import aws_sdk_connectcampaignsv2.types.tag_map

        out["tags"] = aws_sdk_connectcampaignsv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
