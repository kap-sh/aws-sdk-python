"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.campaign_status


class CampaignState(TypedDict):
    campaign_status: NotRequired[
        "aws_sdk_pinpoint.types.campaign_status.CampaignStatus"
    ]
    """<p>The current status of the campaign, or the current status of a treatment that belongs to an A/B test campaign.</p> <p>If a campaign uses A/B testing, the campaign has a status of COMPLETED only if all campaign treatments have a status of COMPLETED. If you delete the segment that's associated with a campaign, the campaign fails and has a status of DELETED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignState) -> dict:
    out: dict = {}
    if "campaign_status" in value:
        import aws_sdk_pinpoint.types.campaign_status

        out["CampaignStatus"] = aws_sdk_pinpoint.types.campaign_status.serialize_json(
            value["campaign_status"]
        )
    return out


def deserialize_json(data: dict) -> CampaignState:
    out: CampaignState = {}  # type: ignore[typeddict-item]
    if "CampaignStatus" in data:
        import aws_sdk_pinpoint.types.campaign_status

        out["campaign_status"] = (
            aws_sdk_pinpoint.types.campaign_status.deserialize_json(
                data["CampaignStatus"]
            )
        )
    return out
