"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetPhoneNumberRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string


class GetPhoneNumberRequest(TypedDict):
    phone_number_id: "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    """<p>The phone number ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPhoneNumberRequest:
    out: GetPhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
