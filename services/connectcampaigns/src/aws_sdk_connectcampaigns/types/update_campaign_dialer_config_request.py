"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#UpdateCampaignDialerConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_id
    import aws_sdk_connectcampaigns.types.dialer_config


class UpdateCampaignDialerConfigRequest(TypedDict):
    id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"
    dialer_config: "aws_sdk_connectcampaigns.types.dialer_config.DialerConfig"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignDialerConfigRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaigns.types.dialer_config

    out["dialerConfig"] = aws_sdk_connectcampaigns.types.dialer_config.serialize_json(
        value["dialer_config"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignDialerConfigRequest:
    out: UpdateCampaignDialerConfigRequest = {}  # type: ignore[typeddict-item]
    if "dialerConfig" in data:
        import aws_sdk_connectcampaigns.types.dialer_config

        out["dialer_config"] = (
            aws_sdk_connectcampaigns.types.dialer_config.deserialize_json(
                data["dialerConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCampaignDialerConfigRequest.dialer_config required"
        )
    return out
