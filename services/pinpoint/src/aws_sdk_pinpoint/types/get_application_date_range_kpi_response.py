"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetApplicationDateRangeKpiResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.application_date_range_kpi_response


class GetApplicationDateRangeKpiResponse(TypedDict, closed=True):
    application_date_range_kpi_response: NotRequired[
        "aws_sdk_pinpoint.types.application_date_range_kpi_response.ApplicationDateRangeKpiResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationDateRangeKpiResponse) -> dict:
    out: dict = {}
    if "application_date_range_kpi_response" in value:
        import aws_sdk_pinpoint.types.application_date_range_kpi_response

        out["ApplicationDateRangeKpiResponse"] = (
            aws_sdk_pinpoint.types.application_date_range_kpi_response.serialize_json(
                value["application_date_range_kpi_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationDateRangeKpiResponse:
    out: GetApplicationDateRangeKpiResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationDateRangeKpiResponse" in data:
        import aws_sdk_pinpoint.types.application_date_range_kpi_response

        out["application_date_range_kpi_response"] = (
            aws_sdk_pinpoint.types.application_date_range_kpi_response.deserialize_json(
                data["ApplicationDateRangeKpiResponse"]
            )
        )
    return out
