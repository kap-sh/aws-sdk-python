"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSegmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetSegmentRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    segment_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSegmentRequest:
    out: GetSegmentRequest = {}  # type: ignore[typeddict-item]
    return out
