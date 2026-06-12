"""Generated from Smithy shape ``com.amazonaws.iotwireless#GsmLocalId``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.bcch
    import aws_sdk_iot_wireless.types.bsic


class GsmLocalId(TypedDict):
    bsic: "aws_sdk_iot_wireless.types.bsic.BSIC"
    """<p>GSM base station identity code (BSIC).</p>"""
    bcch: "aws_sdk_iot_wireless.types.bcch.BCCH"
    """<p>GSM broadcast control channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GsmLocalId) -> dict:
    out: dict = {}
    out["Bsic"] = value["bsic"]
    out["Bcch"] = value["bcch"]
    return out


def deserialize_json(data: dict) -> GsmLocalId:
    out: GsmLocalId = {}  # type: ignore[typeddict-item]
    if "Bsic" in data:
        out["bsic"] = data["Bsic"]
    else:
        raise DeserializationError("GsmLocalId.bsic required")
    if "Bcch" in data:
        out["bcch"] = data["Bcch"]
    else:
        raise DeserializationError("GsmLocalId.bcch required")
    return out
