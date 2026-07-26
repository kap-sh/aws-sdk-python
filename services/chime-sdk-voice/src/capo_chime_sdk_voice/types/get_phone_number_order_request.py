"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetPhoneNumberOrderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.guid_string


class GetPhoneNumberOrderRequest(TypedDict, closed=True):
    phone_number_order_id: "capo_chime_sdk_voice.types.guid_string.GuidString"
    """<p>The ID of the phone number order .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPhoneNumberOrderRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPhoneNumberOrderRequest:
    out: GetPhoneNumberOrderRequest = {}  # type: ignore[typeddict-item]
    return out
