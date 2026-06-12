"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetJourneyExecutionMetricsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetJourneyExecutionMetricsRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    journey_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the journey.</p>"""
    next_token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    page_size: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJourneyExecutionMetricsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJourneyExecutionMetricsRequest:
    out: GetJourneyExecutionMetricsRequest = {}  # type: ignore[typeddict-item]
    return out
