"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSegmentImportJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetSegmentImportJobsRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    page_size: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    segment_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the segment.</p>"""
    token: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The NextToken string that specifies which page of results to return in a paginated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentImportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSegmentImportJobsRequest:
    out: GetSegmentImportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
