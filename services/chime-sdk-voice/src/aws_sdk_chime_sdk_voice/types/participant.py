"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Participant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.e164_phone_number


class Participant(TypedDict, closed=True):
    phone_number: NotRequired[
        "aws_sdk_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The participant's phone number.</p>"""
    proxy_phone_number: NotRequired[
        "aws_sdk_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The participant's proxy phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Participant) -> dict:
    out: dict = {}
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "proxy_phone_number" in value:
        out["ProxyPhoneNumber"] = value["proxy_phone_number"]
    return out


def deserialize_json(data: dict) -> Participant:
    out: Participant = {}  # type: ignore[typeddict-item]
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    if "ProxyPhoneNumber" in data:
        out["proxy_phone_number"] = data["ProxyPhoneNumber"]
    return out
