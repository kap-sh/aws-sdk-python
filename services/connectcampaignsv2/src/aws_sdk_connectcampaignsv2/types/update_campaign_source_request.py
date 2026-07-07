"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.source


class UpdateCampaignSourceRequest(TypedDict, closed=True):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    source: "aws_sdk_connectcampaignsv2.types.source.Source"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignSourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.source

    out["source"] = aws_sdk_connectcampaignsv2.types.source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignSourceRequest:
    out: UpdateCampaignSourceRequest = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_connectcampaignsv2.types.source

        out["source"] = aws_sdk_connectcampaignsv2.types.source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("UpdateCampaignSourceRequest.source required")
    return out
