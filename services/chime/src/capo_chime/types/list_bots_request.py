"""Generated from Smithy shape ``com.amazonaws.chime#ListBotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.result_max
    import capo_chime.types.string


class ListBotsRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    max_results: NotRequired["capo_chime.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call. The default is 10.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBotsRequest:
    out: ListBotsRequest = {}  # type: ignore[typeddict-item]
    return out
