"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ListSipRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.next_token_string
    import aws_sdk_chime_sdk_voice.types.non_empty_string
    import aws_sdk_chime_sdk_voice.types.result_max


class ListSipRulesRequest(TypedDict):
    sip_media_application_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    ]
    """<p>The SIP media application ID.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_voice.types.result_max.ResultMax"]
    """<p>The maximum number of results to return in a single call. Defaults to 100.</p>"""
    next_token: NotRequired[
        "aws_sdk_chime_sdk_voice.types.next_token_string.NextTokenString"
    ]
    """<p>The token used to return the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSipRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSipRulesRequest:
    out: ListSipRulesRequest = {}  # type: ignore[typeddict-item]
    return out
