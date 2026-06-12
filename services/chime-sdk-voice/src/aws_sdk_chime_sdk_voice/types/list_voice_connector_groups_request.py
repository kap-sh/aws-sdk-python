"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListVoiceConnectorGroupsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.result_max
    import aws_sdk_chime_sdk_voice.types.string


class ListVoiceConnectorGroupsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_chime_sdk_voice.types.string.String"]
    """<p>The token used to return the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_voice.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVoiceConnectorGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVoiceConnectorGroupsRequest:
    out: ListVoiceConnectorGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
