"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.campaign


class DescribeCampaignResponse(TypedDict, closed=True):
    campaign: NotRequired["capo_personalize.types.campaign.Campaign"]
    """<note> <p>The <code>latestCampaignUpdate</code> field is only returned when the campaign has had at least one <code>UpdateCampaign</code> call. </p> </note> <p>The properties of the campaign.</p> <note> <p>The <code>latestCampaignUpdate</code> field is only returned when the campaign has had at least one <code>UpdateCampaign</code> call.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCampaignResponse) -> dict:
    out: dict = {}
    if "campaign" in value:
        import capo_personalize.types.campaign

        out["campaign"] = capo_personalize.types.campaign.serialize_aws_json_1_1(
            value["campaign"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCampaignResponse:
    out: DescribeCampaignResponse = {}  # type: ignore[typeddict-item]
    if "campaign" in data:
        import capo_personalize.types.campaign

        out["campaign"] = capo_personalize.types.campaign.deserialize_aws_json_1_1(
            data["campaign"]
        )
    return out
