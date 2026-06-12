"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#GetPhoneNumberResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.phone_number


class GetPhoneNumberResponse(TypedDict):
    phone_number: NotRequired["aws_sdk_chime_sdk_voice.types.phone_number.PhoneNumber"]
    """<p>The phone number details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPhoneNumberResponse) -> dict:
    out: dict = {}
    if "phone_number" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number

        out["PhoneNumber"] = aws_sdk_chime_sdk_voice.types.phone_number.serialize_json(
            value["phone_number"]
        )
    return out


def deserialize_json(data: dict) -> GetPhoneNumberResponse:
    out: GetPhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumber" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number

        out["phone_number"] = (
            aws_sdk_chime_sdk_voice.types.phone_number.deserialize_json(
                data["PhoneNumber"]
            )
        )
    return out
