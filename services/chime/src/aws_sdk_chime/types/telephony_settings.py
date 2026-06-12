"""Generated from Smithy shape ``com.amazonaws.chime#TelephonySettings``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.boolean


class TelephonySettings(TypedDict):
    inbound_calling: "aws_sdk_chime.types.boolean.Boolean"
    """<p>Allows or denies inbound calling.</p>"""
    outbound_calling: "aws_sdk_chime.types.boolean.Boolean"
    """<p>Allows or denies outbound calling.</p>"""
    sms: "aws_sdk_chime.types.boolean.Boolean"
    """<p>Allows or denies SMS messaging.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelephonySettings) -> dict:
    out: dict = {}
    out["InboundCalling"] = value["inbound_calling"]
    out["OutboundCalling"] = value["outbound_calling"]
    out["SMS"] = value["sms"]
    return out


def deserialize_json(data: dict) -> TelephonySettings:
    out: TelephonySettings = {}  # type: ignore[typeddict-item]
    if "InboundCalling" in data:
        out["inbound_calling"] = data["InboundCalling"]
    else:
        raise DeserializationError("TelephonySettings.inbound_calling required")
    if "OutboundCalling" in data:
        out["outbound_calling"] = data["OutboundCalling"]
    else:
        raise DeserializationError("TelephonySettings.outbound_calling required")
    if "SMS" in data:
        out["sms"] = data["SMS"]
    else:
        raise DeserializationError("TelephonySettings.sms required")
    return out
