"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.schedule


class UpdateCampaignScheduleRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    schedule: "capo_connectcampaignsv2.types.schedule.Schedule"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignScheduleRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.schedule

    out["schedule"] = capo_connectcampaignsv2.types.schedule.serialize_json(
        value["schedule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignScheduleRequest:
    out: UpdateCampaignScheduleRequest = {}  # type: ignore[typeddict-item]
    if "schedule" in data:
        import capo_connectcampaignsv2.types.schedule

        out["schedule"] = capo_connectcampaignsv2.types.schedule.deserialize_json(
            data["schedule"]
        )
    else:
        raise DeserializationError("UpdateCampaignScheduleRequest.schedule required")
    return out
