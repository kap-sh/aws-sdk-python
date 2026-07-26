"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetSipMediaApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.non_empty_string


class GetSipMediaApplicationRequest(TypedDict, closed=True):
    sip_media_application_id: (
        "capo_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSipMediaApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSipMediaApplicationRequest:
    out: GetSipMediaApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
