"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListSipMediaApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.next_token_string
    import capo_chime_sdk_voice.types.result_max


class ListSipMediaApplicationsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_chime_sdk_voice.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call. Defaults to 100.</p>"""
    next_token: NotRequired[
        "capo_chime_sdk_voice.types.next_token_string.NextTokenString"
    ]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSipMediaApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSipMediaApplicationsRequest:
    out: ListSipMediaApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
