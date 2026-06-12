"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignChannelSubtypeConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.channel_subtype_config


class UpdateCampaignChannelSubtypeConfigRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    channel_subtype_config: (
        "aws_sdk_connectcampaignsv2.types.channel_subtype_config.ChannelSubtypeConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignChannelSubtypeConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.channel_subtype_config

    out["channelSubtypeConfig"] = (
        aws_sdk_connectcampaignsv2.types.channel_subtype_config.serialize_json(
            value["channel_subtype_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignChannelSubtypeConfigRequest:
    out: UpdateCampaignChannelSubtypeConfigRequest = {}  # type: ignore[typeddict-item]
    if "channelSubtypeConfig" in data:
        import aws_sdk_connectcampaignsv2.types.channel_subtype_config

        out["channel_subtype_config"] = (
            aws_sdk_connectcampaignsv2.types.channel_subtype_config.deserialize_json(
                data["channelSubtypeConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCampaignChannelSubtypeConfigRequest.channel_subtype_config required"
        )
    return out
