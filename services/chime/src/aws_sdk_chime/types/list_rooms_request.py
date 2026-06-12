"""Generated from Smithy shape ``com.amazonaws.chime#ListRoomsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.result_max
    import aws_sdk_chime.types.string


class ListRoomsRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    member_id: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The member ID (user ID or bot ID).</p>"""
    max_results: NotRequired["aws_sdk_chime.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRoomsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRoomsRequest:
    out: ListRoomsRequest = {}  # type: ignore[typeddict-item]
    return out
