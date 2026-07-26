"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#DeletePhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_non_empty_string


class DeletePhoneNumberRequest(TypedDict, closed=True):
    phone_number_id: (
        "capo_chime_sdk_voice.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>The phone number ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePhoneNumberRequest:
    out: DeletePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
