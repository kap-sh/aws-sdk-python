"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyExecutionMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journey_execution_metrics_response


class GetJourneyExecutionMetricsResponse(TypedDict):
    journey_execution_metrics_response: NotRequired[
        "aws_sdk_pinpoint.types.journey_execution_metrics_response.JourneyExecutionMetricsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyExecutionMetricsResponse) -> dict:
    out: dict = {}
    if "journey_execution_metrics_response" in value:
        import aws_sdk_pinpoint.types.journey_execution_metrics_response

        out["JourneyExecutionMetricsResponse"] = (
            aws_sdk_pinpoint.types.journey_execution_metrics_response.serialize_json(
                value["journey_execution_metrics_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyExecutionMetricsResponse:
    out: GetJourneyExecutionMetricsResponse = {}  # type: ignore[typeddict-item]
    if "JourneyExecutionMetricsResponse" in data:
        import aws_sdk_pinpoint.types.journey_execution_metrics_response

        out["journey_execution_metrics_response"] = (
            aws_sdk_pinpoint.types.journey_execution_metrics_response.deserialize_json(
                data["JourneyExecutionMetricsResponse"]
            )
        )
    return out
