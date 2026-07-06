"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreatePhoneNumberOrderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.phone_number_order


class CreatePhoneNumberOrderResponse(TypedDict, closed=True):
    phone_number_order: NotRequired[
        "aws_sdk_chime_sdk_voice.types.phone_number_order.PhoneNumberOrder"
    ]
    """<p>The phone number order details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePhoneNumberOrderResponse) -> dict:
    out: dict = {}
    if "phone_number_order" in value:
        import aws_sdk_chime_sdk_voice.types.phone_number_order

        out["PhoneNumberOrder"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_order.serialize_json(
                value["phone_number_order"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreatePhoneNumberOrderResponse:
    out: CreatePhoneNumberOrderResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumberOrder" in data:
        import aws_sdk_chime_sdk_voice.types.phone_number_order

        out["phone_number_order"] = (
            aws_sdk_chime_sdk_voice.types.phone_number_order.deserialize_json(
                data["PhoneNumberOrder"]
            )
        )
    return out
