"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#RestorePhoneNumberRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string


class RestorePhoneNumberRequest(TypedDict):
    phone_number_id: "aws_sdk_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    """<p>The ID of the phone number being restored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestorePhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestorePhoneNumberRequest:
    out: RestorePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
