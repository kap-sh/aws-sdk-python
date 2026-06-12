"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignEntryLimitsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.entry_limits_config


class UpdateCampaignEntryLimitsRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    entry_limits_config: (
        "aws_sdk_connectcampaignsv2.types.entry_limits_config.EntryLimitsConfig"
    )


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignEntryLimitsRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.entry_limits_config

    out["entryLimitsConfig"] = (
        aws_sdk_connectcampaignsv2.types.entry_limits_config.serialize_json(
            value["entry_limits_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignEntryLimitsRequest:
    out: UpdateCampaignEntryLimitsRequest = {}  # type: ignore[typeddict-item]
    if "entryLimitsConfig" in data:
        import aws_sdk_connectcampaignsv2.types.entry_limits_config

        out["entry_limits_config"] = (
            aws_sdk_connectcampaignsv2.types.entry_limits_config.deserialize_json(
                data["entryLimitsConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCampaignEntryLimitsRequest.entry_limits_config required"
        )
    return out
