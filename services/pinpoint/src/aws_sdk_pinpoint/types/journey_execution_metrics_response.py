"""Generated from Smithy shape ``com.amazonaws.pinpoint#JourneyExecutionMetricsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.map_of__string


class JourneyExecutionMetricsResponse(TypedDict):
    application_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the application that the metric applies to.</p>"""
    journey_id: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the journey that the metric applies to.</p>"""
    last_evaluated_time: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The date and time, in ISO 8601 format, when Amazon Pinpoint last evaluated the journey and updated the data for the metric.</p>"""
    metrics: NotRequired["aws_sdk_pinpoint.types.map_of__string.MapOf__string"]
    """<p>A JSON object that contains the results of the query. For information about the structure and contents of the results, see the <a href=\"https://docs.aws.amazon.com//pinpoint/latest/developerguide/analytics-standard-metrics.html\">Amazon Pinpoint Developer Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JourneyExecutionMetricsResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "journey_id" in value:
        out["JourneyId"] = value["journey_id"]
    if "last_evaluated_time" in value:
        out["LastEvaluatedTime"] = value["last_evaluated_time"]
    if "metrics" in value:
        import aws_sdk_pinpoint.types.map_of__string

        out["Metrics"] = aws_sdk_pinpoint.types.map_of__string.serialize_json(
            value["metrics"]
        )
    return out


def deserialize_json(data: dict) -> JourneyExecutionMetricsResponse:
    out: JourneyExecutionMetricsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "JourneyId" in data:
        out["journey_id"] = data["JourneyId"]
    if "LastEvaluatedTime" in data:
        out["last_evaluated_time"] = data["LastEvaluatedTime"]
    if "Metrics" in data:
        import aws_sdk_pinpoint.types.map_of__string

        out["metrics"] = aws_sdk_pinpoint.types.map_of__string.deserialize_json(
            data["Metrics"]
        )
    return out
