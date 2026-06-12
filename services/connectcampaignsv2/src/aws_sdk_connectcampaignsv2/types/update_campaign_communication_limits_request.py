"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignCommunicationLimitsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.communication_limits_config


class UpdateCampaignCommunicationLimitsRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    communication_limits_override: "aws_sdk_connectcampaignsv2.types.communication_limits_config.CommunicationLimitsConfig"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignCommunicationLimitsRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.communication_limits_config

    out["communicationLimitsOverride"] = (
        aws_sdk_connectcampaignsv2.types.communication_limits_config.serialize_json(
            value["communication_limits_override"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignCommunicationLimitsRequest:
    out: UpdateCampaignCommunicationLimitsRequest = {}  # type: ignore[typeddict-item]
    if "communicationLimitsOverride" in data:
        import aws_sdk_connectcampaignsv2.types.communication_limits_config

        out["communication_limits_override"] = (
            aws_sdk_connectcampaignsv2.types.communication_limits_config.deserialize_json(
                data["communicationLimitsOverride"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCampaignCommunicationLimitsRequest.communication_limits_override required"
        )
    return out
