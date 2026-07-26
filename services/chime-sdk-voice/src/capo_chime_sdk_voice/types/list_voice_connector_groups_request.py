"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceConnectorGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.result_max
    import capo_chime_sdk_voice.types.string


class ListVoiceConnectorGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""
    max_results: NotRequired["capo_chime_sdk_voice.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceConnectorGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVoiceConnectorGroupsRequest:
    out: ListVoiceConnectorGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
