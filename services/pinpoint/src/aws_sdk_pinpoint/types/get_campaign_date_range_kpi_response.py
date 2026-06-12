"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetCampaignDateRangeKpiResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.campaign_date_range_kpi_response


class GetCampaignDateRangeKpiResponse(TypedDict):
    campaign_date_range_kpi_response: NotRequired[
        "aws_sdk_pinpoint.types.campaign_date_range_kpi_response.CampaignDateRangeKpiResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignDateRangeKpiResponse) -> dict:
    out: dict = {}
    if "campaign_date_range_kpi_response" in value:
        import aws_sdk_pinpoint.types.campaign_date_range_kpi_response

        out["CampaignDateRangeKpiResponse"] = (
            aws_sdk_pinpoint.types.campaign_date_range_kpi_response.serialize_json(
                value["campaign_date_range_kpi_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCampaignDateRangeKpiResponse:
    out: GetCampaignDateRangeKpiResponse = {}  # type: ignore[typeddict-item]
    if "CampaignDateRangeKpiResponse" in data:
        import aws_sdk_pinpoint.types.campaign_date_range_kpi_response

        out["campaign_date_range_kpi_response"] = (
            aws_sdk_pinpoint.types.campaign_date_range_kpi_response.deserialize_json(
                data["CampaignDateRangeKpiResponse"]
            )
        )
    return out
