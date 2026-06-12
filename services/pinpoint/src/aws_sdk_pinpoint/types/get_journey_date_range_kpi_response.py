"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyDateRangeKpiResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journey_date_range_kpi_response


class GetJourneyDateRangeKpiResponse(TypedDict):
    journey_date_range_kpi_response: NotRequired[
        "aws_sdk_pinpoint.types.journey_date_range_kpi_response.JourneyDateRangeKpiResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyDateRangeKpiResponse) -> dict:
    out: dict = {}
    if "journey_date_range_kpi_response" in value:
        import aws_sdk_pinpoint.types.journey_date_range_kpi_response

        out["JourneyDateRangeKpiResponse"] = (
            aws_sdk_pinpoint.types.journey_date_range_kpi_response.serialize_json(
                value["journey_date_range_kpi_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyDateRangeKpiResponse:
    out: GetJourneyDateRangeKpiResponse = {}  # type: ignore[typeddict-item]
    if "JourneyDateRangeKpiResponse" in data:
        import aws_sdk_pinpoint.types.journey_date_range_kpi_response

        out["journey_date_range_kpi_response"] = (
            aws_sdk_pinpoint.types.journey_date_range_kpi_response.deserialize_json(
                data["JourneyDateRangeKpiResponse"]
            )
        )
    return out
