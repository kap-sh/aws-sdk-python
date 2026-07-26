"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyRunExecutionMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.journey_run_execution_metrics_response


class GetJourneyRunExecutionMetricsResponse(TypedDict, closed=True):
    journey_run_execution_metrics_response: NotRequired[
        "capo_pinpoint.types.journey_run_execution_metrics_response.JourneyRunExecutionMetricsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyRunExecutionMetricsResponse) -> dict:
    out: dict = {}
    if "journey_run_execution_metrics_response" in value:
        import capo_pinpoint.types.journey_run_execution_metrics_response

        out["JourneyRunExecutionMetricsResponse"] = (
            capo_pinpoint.types.journey_run_execution_metrics_response.serialize_json(
                value["journey_run_execution_metrics_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyRunExecutionMetricsResponse:
    out: GetJourneyRunExecutionMetricsResponse = {}  # type: ignore[typeddict-item]
    if "JourneyRunExecutionMetricsResponse" in data:
        import capo_pinpoint.types.journey_run_execution_metrics_response

        out["journey_run_execution_metrics_response"] = (
            capo_pinpoint.types.journey_run_execution_metrics_response.deserialize_json(
                data["JourneyRunExecutionMetricsResponse"]
            )
        )
    return out
