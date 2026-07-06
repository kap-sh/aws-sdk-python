"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeleteSipMediaApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class DeleteSipMediaApplicationRequest(TypedDict, closed=True):
    sip_media_application_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSipMediaApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSipMediaApplicationRequest:
    out: DeleteSipMediaApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
