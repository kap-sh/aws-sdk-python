"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyExecutionMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.journey_execution_metrics_response


class GetJourneyExecutionMetricsResponse(TypedDict, closed=True):
    journey_execution_metrics_response: NotRequired[
        "capo_pinpoint.types.journey_execution_metrics_response.JourneyExecutionMetricsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyExecutionMetricsResponse) -> dict:
    out: dict = {}
    if "journey_execution_metrics_response" in value:
        import capo_pinpoint.types.journey_execution_metrics_response

        out["JourneyExecutionMetricsResponse"] = (
            capo_pinpoint.types.journey_execution_metrics_response.serialize_json(
                value["journey_execution_metrics_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyExecutionMetricsResponse:
    out: GetJourneyExecutionMetricsResponse = {}  # type: ignore[typeddict-item]
    if "JourneyExecutionMetricsResponse" in data:
        import capo_pinpoint.types.journey_execution_metrics_response

        out["journey_execution_metrics_response"] = (
            capo_pinpoint.types.journey_execution_metrics_response.deserialize_json(
                data["JourneyExecutionMetricsResponse"]
            )
        )
    return out
