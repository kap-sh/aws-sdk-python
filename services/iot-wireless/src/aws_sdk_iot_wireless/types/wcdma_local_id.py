"""Generated from Smithy shape ``com.amazonaws.iotwireless#WcdmaLocalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.psc
    import aws_sdk_iot_wireless.types.uarfcndl


class WcdmaLocalId(TypedDict, closed=True):
    uarfcndl: "aws_sdk_iot_wireless.types.uarfcndl.UARFCNDL"
    """<p>WCDMA UTRA Absolute RF Channel Number downlink.</p>"""
    psc: "aws_sdk_iot_wireless.types.psc.PSC"
    """<p>Primary Scrambling Code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WcdmaLocalId) -> dict:
    out: dict = {}
    out["Uarfcndl"] = value["uarfcndl"]
    out["Psc"] = value["psc"]
    return out


def deserialize_json(data: dict) -> WcdmaLocalId:
    out: WcdmaLocalId = {}  # type: ignore[typeddict-item]
    if "Uarfcndl" in data:
        out["uarfcndl"] = data["Uarfcndl"]
    else:
        raise DeserializationError("WcdmaLocalId.uarfcndl required")
    if "Psc" in data:
        out["psc"] = data["Psc"]
    else:
        raise DeserializationError("WcdmaLocalId.psc required")
    return out
