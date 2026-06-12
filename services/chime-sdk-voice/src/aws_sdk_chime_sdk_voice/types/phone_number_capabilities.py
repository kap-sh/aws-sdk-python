"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberCapabilities``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.nullable_boolean


class PhoneNumberCapabilities(TypedDict):
    inbound_call: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Allows or denies inbound calling for the specified phone number.</p>"""
    outbound_call: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Allows or denies outbound calling for the specified phone number.</p>"""
    inbound_sms: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Allows or denies inbound SMS messaging for the specified phone number.</p>"""
    outbound_sms: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Allows or denies outbound SMS messaging for the specified phone number.</p>"""
    inbound_mms: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Allows or denies inbound MMS messaging for the specified phone number.</p>"""
    outbound_mms: NotRequired[
        "aws_sdk_chime_sdk_voice.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Allows or denies inbound MMS messaging for the specified phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberCapabilities) -> dict:
    out: dict = {}
    if "inbound_call" in value:
        out["InboundCall"] = value["inbound_call"]
    if "outbound_call" in value:
        out["OutboundCall"] = value["outbound_call"]
    if "inbound_sms" in value:
        out["InboundSMS"] = value["inbound_sms"]
    if "outbound_sms" in value:
        out["OutboundSMS"] = value["outbound_sms"]
    if "inbound_mms" in value:
        out["InboundMMS"] = value["inbound_mms"]
    if "outbound_mms" in value:
        out["OutboundMMS"] = value["outbound_mms"]
    return out


def deserialize_json(data: dict) -> PhoneNumberCapabilities:
    out: PhoneNumberCapabilities = {}  # type: ignore[typeddict-item]
    if "InboundCall" in data:
        out["inbound_call"] = data["InboundCall"]
    if "OutboundCall" in data:
        out["outbound_call"] = data["OutboundCall"]
    if "InboundSMS" in data:
        out["inbound_sms"] = data["InboundSMS"]
    if "OutboundSMS" in data:
        out["outbound_sms"] = data["OutboundSMS"]
    if "InboundMMS" in data:
        out["inbound_mms"] = data["InboundMMS"]
    if "OutboundMMS" in data:
        out["outbound_mms"] = data["OutboundMMS"]
    return out
