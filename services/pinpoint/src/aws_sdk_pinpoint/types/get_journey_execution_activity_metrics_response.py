"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyExecutionActivityMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.journey_execution_activity_metrics_response


class GetJourneyExecutionActivityMetricsResponse(TypedDict):
    journey_execution_activity_metrics_response: NotRequired[
        "aws_sdk_pinpoint.types.journey_execution_activity_metrics_response.JourneyExecutionActivityMetricsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyExecutionActivityMetricsResponse) -> dict:
    out: dict = {}
    if "journey_execution_activity_metrics_response" in value:
        import aws_sdk_pinpoint.types.journey_execution_activity_metrics_response

        out["JourneyExecutionActivityMetricsResponse"] = (
            aws_sdk_pinpoint.types.journey_execution_activity_metrics_response.serialize_json(
                value["journey_execution_activity_metrics_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetJourneyExecutionActivityMetricsResponse:
    out: GetJourneyExecutionActivityMetricsResponse = {}  # type: ignore[typeddict-item]
    if "JourneyExecutionActivityMetricsResponse" in data:
        import aws_sdk_pinpoint.types.journey_execution_activity_metrics_response

        out["journey_execution_activity_metrics_response"] = (
            aws_sdk_pinpoint.types.journey_execution_activity_metrics_response.deserialize_json(
                data["JourneyExecutionActivityMetricsResponse"]
            )
        )
    return out
