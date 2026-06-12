"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyRunExecutionMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journey_run_execution_metrics_response


class GetJourneyRunExecutionMetricsResponse(TypedDict):
    journey_run_execution_metrics_response: NotRequired[
        "aws_sdk_pinpoint.types.journey_run_execution_metrics_response.JourneyRunExecutionMetricsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyRunExecutionMetricsResponse) -> dict:
    out: dict = {}
    if "journey_run_execution_metrics_response" in value:
        import aws_sdk_pinpoint.types.journey_run_execution_metrics_response

        out["JourneyRunExecutionMetricsResponse"] = (
            aws_sdk_pinpoint.types.journey_run_execution_metrics_response.serialize_json(
                value["journey_run_execution_metrics_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyRunExecutionMetricsResponse:
    out: GetJourneyRunExecutionMetricsResponse = {}  # type: ignore[typeddict-item]
    if "JourneyRunExecutionMetricsResponse" in data:
        import aws_sdk_pinpoint.types.journey_run_execution_metrics_response

        out["journey_run_execution_metrics_response"] = (
            aws_sdk_pinpoint.types.journey_run_execution_metrics_response.deserialize_json(
                data["JourneyRunExecutionMetricsResponse"]
            )
        )
    return out
