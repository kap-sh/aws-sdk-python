"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#UpdatePhoneNumberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.phone_number


class UpdatePhoneNumberResponse(TypedDict, closed=True):
    phone_number: NotRequired["aws_sdk_chime_sdk_voice.types.phone_number.PhoneNumber"]
    """<p>The updated phone number details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberResponse) -> dict:
    out: dict = {}
    if "phone_number" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number

        out["PhoneNumber"] = aws_sdk_chime_sdk_voice.types.phone_number.serialize_json(
            value["phone_number"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberResponse:
    out: UpdatePhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumber" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number

        out["phone_number"] = (
            aws_sdk_chime_sdk_voice.types.phone_number.deserialize_json(
                data["PhoneNumber"]
            )
        )
    return out
