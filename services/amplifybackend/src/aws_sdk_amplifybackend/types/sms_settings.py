"""Generated from Smithy shape ``com.amazonaws.amplifybackend#SmsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string


class SmsSettings(TypedDict, closed=True):
    sms_message: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The contents of the SMS message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SmsSettings) -> dict:
    out: dict = {}
    if "sms_message" in value:
        out["smsMessage"] = value["sms_message"]
    return out


def deserialize_json(data: dict) -> SmsSettings:
    out: SmsSettings = {}  # type: ignore[typeddict-item]
    if "smsMessage" in data:
        out["sms_message"] = data["smsMessage"]
    return out
