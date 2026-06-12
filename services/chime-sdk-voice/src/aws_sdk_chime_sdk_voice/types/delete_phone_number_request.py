"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeletePhoneNumberRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string


class DeletePhoneNumberRequest(TypedDict):
    phone_number_id: "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    """<p>The phone number ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePhoneNumberRequest:
    out: DeletePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
