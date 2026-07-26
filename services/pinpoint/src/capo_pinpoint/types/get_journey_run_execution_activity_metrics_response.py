"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyRunExecutionActivityMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.journey_run_execution_activity_metrics_response


class GetJourneyRunExecutionActivityMetricsResponse(TypedDict, closed=True):
    journey_run_execution_activity_metrics_response: NotRequired[
        "capo_pinpoint.types.journey_run_execution_activity_metrics_response.JourneyRunExecutionActivityMetricsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyRunExecutionActivityMetricsResponse) -> dict:
    out: dict = {}
    if "journey_run_execution_activity_metrics_response" in value:
        import capo_pinpoint.types.journey_run_execution_activity_metrics_response

        out["JourneyRunExecutionActivityMetricsResponse"] = (
            capo_pinpoint.types.journey_run_execution_activity_metrics_response.serialize_json(
                value["journey_run_execution_activity_metrics_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyRunExecutionActivityMetricsResponse:
    out: GetJourneyRunExecutionActivityMetricsResponse = {}  # type: ignore[typeddict-item]
    if "JourneyRunExecutionActivityMetricsResponse" in data:
        import capo_pinpoint.types.journey_run_execution_activity_metrics_response

        out["journey_run_execution_activity_metrics_response"] = (
            capo_pinpoint.types.journey_run_execution_activity_metrics_response.deserialize_json(
                data["JourneyRunExecutionActivityMetricsResponse"]
            )
        )
    return out
