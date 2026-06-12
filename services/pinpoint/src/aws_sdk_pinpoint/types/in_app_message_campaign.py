"""Generated from Smithy shape ``com.amazonaws.pinpoint#InAppMessageCampaign``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__integer
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.in_app_campaign_schedule
    import aws_sdk_pinpoint.types.in_app_message


class InAppMessageCampaign(TypedDict):
    campaign_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Campaign id of the corresponding campaign.</p>"""
    daily_cap: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>Daily cap which controls the number of times any in-app messages can be shown to the endpoint during a day.</p>"""
    in_app_message: NotRequired["aws_sdk_pinpoint.types.in_app_message.InAppMessage"]
    """<p>In-app message content with all fields required for rendering an in-app message.</p>"""
    priority: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>Priority of the in-app message.</p>"""
    schedule: NotRequired[
        "aws_sdk_pinpoint.types.in_app_campaign_schedule.InAppCampaignSchedule"
    ]
    """<p>Schedule of the campaign.</p>"""
    session_cap: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>Session cap which controls the number of times an in-app message can be shown to the endpoint during an application session.</p>"""
    total_cap: NotRequired["aws_sdk_pinpoint.types.__integer.__integer"]
    """<p>Total cap which controls the number of times an in-app message can be shown to the endpoint.</p>"""
    treatment_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>Treatment id of the campaign.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InAppMessageCampaign) -> dict:
    out: dict = {}
    if "campaign_id" in value:
        out["CampaignId"] = value["campaign_id"]
    if "daily_cap" in value:
        out["DailyCap"] = value["daily_cap"]
    if "in_app_message" in value:
        import aws_sdk_pinpoint.types.in_app_message

        out["InAppMessage"] = aws_sdk_pinpoint.types.in_app_message.serialize_json(
            value["in_app_message"]
        )
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "schedule" in value:
        import aws_sdk_pinpoint.types.in_app_campaign_schedule

        out["Schedule"] = (
            aws_sdk_pinpoint.types.in_app_campaign_schedule.serialize_json(
                value["schedule"]
            )
        )
    if "session_cap" in value:
        out["SessionCap"] = value["session_cap"]
    if "total_cap" in value:
        out["TotalCap"] = value["total_cap"]
    if "treatment_id" in value:
        out["TreatmentId"] = value["treatment_id"]
    return out


def deserialize_json(data: dict) -> InAppMessageCampaign:
    out: InAppMessageCampaign = {}  # type: ignore[typeddict-item]
    if "CampaignId" in data:
        out["campaign_id"] = data["CampaignId"]
    if "DailyCap" in data:
        out["daily_cap"] = data["DailyCap"]
    if "InAppMessage" in data:
        import aws_sdk_pinpoint.types.in_app_message

        out["in_app_message"] = aws_sdk_pinpoint.types.in_app_message.deserialize_json(
            data["InAppMessage"]
        )
    if "Priority" in data:
        out["priority"] = data["Priority"]
    if "Schedule" in data:
        import aws_sdk_pinpoint.types.in_app_campaign_schedule

        out["schedule"] = (
            aws_sdk_pinpoint.types.in_app_campaign_schedule.deserialize_json(
                data["Schedule"]
            )
        )
    if "SessionCap" in data:
        out["session_cap"] = data["SessionCap"]
    if "TotalCap" in data:
        out["total_cap"] = data["TotalCap"]
    if "TreatmentId" in data:
        out["treatment_id"] = data["TreatmentId"]
    return out
