"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListPhoneNumberOrdersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.result_max
    import capo_chime_sdk_voice.types.string


class ListPhoneNumberOrdersRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The token used to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_chime_sdk_voice.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPhoneNumberOrdersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPhoneNumberOrdersRequest:
    out: ListPhoneNumberOrdersRequest = {}  # type: ignore[typeddict-item]
    return out
