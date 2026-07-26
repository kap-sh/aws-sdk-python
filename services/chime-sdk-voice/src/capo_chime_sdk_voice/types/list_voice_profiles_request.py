"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string256
    import capo_chime_sdk_voice.types.result_max
    import capo_chime_sdk_voice.types.string


class ListVoiceProfilesRequest(TypedDict, closed=True):
    voice_profile_domain_id: (
        "capo_chime_sdk_voice.types.non_empty_string256.NonEmptyString256"
    )
    """<p>The ID of the voice profile domain.</p>"""
    next_token: NotRequired["capo_chime_sdk_voice.types.string.String"]
    """<p>The token used to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_chime_sdk_voice.types.result_max.ResultMax"]
    """<p>The maximum number of results in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVoiceProfilesRequest:
    out: ListVoiceProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
