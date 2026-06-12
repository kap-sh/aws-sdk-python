"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignCommunicationTimeRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.communication_time_config


class UpdateCampaignCommunicationTimeRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    communication_time_config: "aws_sdk_connectcampaignsv2.types.communication_time_config.CommunicationTimeConfig"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignCommunicationTimeRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.communication_time_config

    out["communicationTimeConfig"] = (
        aws_sdk_connectcampaignsv2.types.communication_time_config.serialize_json(
            value["communication_time_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignCommunicationTimeRequest:
    out: UpdateCampaignCommunicationTimeRequest = {}  # type: ignore[typeddict-item]
    if "communicationTimeConfig" in data:
        import aws_sdk_connectcampaignsv2.types.communication_time_config

        out["communication_time_config"] = (
            aws_sdk_connectcampaignsv2.types.communication_time_config.deserialize_json(
                data["communicationTimeConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCampaignCommunicationTimeRequest.communication_time_config required"
        )
    return out
