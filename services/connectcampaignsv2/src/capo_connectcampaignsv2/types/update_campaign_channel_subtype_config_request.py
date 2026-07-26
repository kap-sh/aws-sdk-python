"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignChannelSubtypeConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.channel_subtype_config


class UpdateCampaignChannelSubtypeConfigRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    channel_subtype_config: (
        "capo_connectcampaignsv2.types.channel_subtype_config.ChannelSubtypeConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignChannelSubtypeConfigRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.channel_subtype_config

    out["channelSubtypeConfig"] = (
        capo_connectcampaignsv2.types.channel_subtype_config.serialize_json(
            value["channel_subtype_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignChannelSubtypeConfigRequest:
    out: UpdateCampaignChannelSubtypeConfigRequest = {}  # type: ignore[typeddict-item]
    if "channelSubtypeConfig" in data:
        import capo_connectcampaignsv2.types.channel_subtype_config

        out["channel_subtype_config"] = (
            capo_connectcampaignsv2.types.channel_subtype_config.deserialize_json(
                data["channelSubtypeConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCampaignChannelSubtypeConfigRequest.channel_subtype_config required"
        )
    return out
