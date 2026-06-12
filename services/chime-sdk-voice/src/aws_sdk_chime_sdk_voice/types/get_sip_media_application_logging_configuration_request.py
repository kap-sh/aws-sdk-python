"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetSipMediaApplicationLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string


class GetSipMediaApplicationLoggingConfigurationRequest(TypedDict):
    sip_media_application_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string.NonEmptyString"
    )
    """<p>The SIP media application ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSipMediaApplicationLoggingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSipMediaApplicationLoggingConfigurationRequest:
    out: GetSipMediaApplicationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
