"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ListAttendeesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.guid_string
    import aws_sdk_chime_sdk_meetings.types.result_max
    import aws_sdk_chime_sdk_meetings.types.string


class ListAttendeesRequest(TypedDict, closed=True):
    meeting_id: "aws_sdk_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK meeting ID.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_meetings.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_meetings.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttendeesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAttendeesRequest:
    out: ListAttendeesRequest = {}  # type: ignore[typeddict-item]
    return out
