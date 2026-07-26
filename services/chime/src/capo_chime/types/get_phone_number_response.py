"""Generated from Smithy shape ``com.amazonaws.chime#GetPhoneNumberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.phone_number


class GetPhoneNumberResponse(TypedDict, closed=True):
    phone_number: NotRequired["capo_chime.types.phone_number.PhoneNumber"]
    """<p>The phone number details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPhoneNumberResponse) -> dict:
    out: dict = {}
    if "phone_number" in value:
        import capo_chime.types.phone_number

        out["PhoneNumber"] = capo_chime.types.phone_number.serialize_json(
            value["phone_number"]
        )
    return out


def deserialize_json(data: dict) -> GetPhoneNumberResponse:
    out: GetPhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumber" in data:
        import capo_chime.types.phone_number

        out["phone_number"] = capo_chime.types.phone_number.deserialize_json(
            data["PhoneNumber"]
        )
    return out
