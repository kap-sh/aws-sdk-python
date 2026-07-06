"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyExecutionActivityMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetJourneyExecutionActivityMetricsRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    journey_activity_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the journey activity.</p>"""
    journey_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the journey.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    page_size: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyExecutionActivityMetricsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJourneyExecutionActivityMetricsRequest:
    out: GetJourneyExecutionActivityMetricsRequest = {}  # type: ignore[typeddict-item]
    return out
