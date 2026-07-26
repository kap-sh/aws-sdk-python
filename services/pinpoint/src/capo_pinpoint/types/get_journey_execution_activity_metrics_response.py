"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyExecutionActivityMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.journey_execution_activity_metrics_response


class GetJourneyExecutionActivityMetricsResponse(TypedDict, closed=True):
    journey_execution_activity_metrics_response: NotRequired[
        "capo_pinpoint.types.journey_execution_activity_metrics_response.JourneyExecutionActivityMetricsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyExecutionActivityMetricsResponse) -> dict:
    out: dict = {}
    if "journey_execution_activity_metrics_response" in value:
        import capo_pinpoint.types.journey_execution_activity_metrics_response

        out["JourneyExecutionActivityMetricsResponse"] = (
            capo_pinpoint.types.journey_execution_activity_metrics_response.serialize_json(
                value["journey_execution_activity_metrics_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyExecutionActivityMetricsResponse:
    out: GetJourneyExecutionActivityMetricsResponse = {}  # type: ignore[typeddict-item]
    if "JourneyExecutionActivityMetricsResponse" in data:
        import capo_pinpoint.types.journey_execution_activity_metrics_response

        out["journey_execution_activity_metrics_response"] = (
            capo_pinpoint.types.journey_execution_activity_metrics_response.deserialize_json(
                data["JourneyExecutionActivityMetricsResponse"]
            )
        )
    return out
