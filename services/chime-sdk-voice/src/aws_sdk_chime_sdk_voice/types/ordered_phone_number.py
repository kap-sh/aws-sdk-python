"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#OrderedPhoneNumber``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.e164_phone_number
    import aws_sdk_chime_sdk_voice.types.ordered_phone_number_status


class OrderedPhoneNumber(TypedDict):
    e164_phone_number: NotRequired[
        "aws_sdk_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The phone number, in E.164 format.</p>"""
    status: NotRequired[
        "aws_sdk_chime_sdk_voice.types.ordered_phone_number_status.OrderedPhoneNumberStatus"
    ]
    """<p>The phone number status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrderedPhoneNumber) -> dict:
    out: dict = {}
    if "e164_phone_number" in value:
        out["E164PhoneNumber"] = value["e164_phone_number"]
    if "status" in value:
        import aws_sdk_chime_sdk_voice.types.ordered_phone_number_status

        out["Status"] = (
            aws_sdk_chime_sdk_voice.types.ordered_phone_number_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> OrderedPhoneNumber:
    out: OrderedPhoneNumber = {}  # type: ignore[typeddict-item]
    if "E164PhoneNumber" in data:
        out["e164_phone_number"] = data["E164PhoneNumber"]
    if "Status" in data:
        import aws_sdk_chime_sdk_voice.types.ordered_phone_number_status

        out["status"] = (
            aws_sdk_chime_sdk_voice.types.ordered_phone_number_status.deserialize_json(
                data["Status"]
            )
        )
    return out
