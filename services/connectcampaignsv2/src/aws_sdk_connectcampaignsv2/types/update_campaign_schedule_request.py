"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#UpdateCampaignScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.schedule


class UpdateCampaignScheduleRequest(TypedDict, closed=True):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    schedule: "aws_sdk_connectcampaignsv2.types.schedule.Schedule"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignScheduleRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.schedule

    out["schedule"] = aws_sdk_connectcampaignsv2.types.schedule.serialize_json(
        value["schedule"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCampaignScheduleRequest:
    out: UpdateCampaignScheduleRequest = {}  # type: ignore[typeddict-item]
    if "schedule" in data:
        import aws_sdk_connectcampaignsv2.types.schedule

        out["schedule"] = aws_sdk_connectcampaignsv2.types.schedule.deserialize_json(
            data["schedule"]
        )
    else:
        raise DeserializationError("UpdateCampaignScheduleRequest.schedule required")
    return out
