"""Generated from Smithy shape ``com.amazonaws.iotwireless#CdmaLocalId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.cdma_channel
    import aws_sdk_iot_wireless.types.pn_offset


class CdmaLocalId(TypedDict, closed=True):
    pn_offset: "aws_sdk_iot_wireless.types.pn_offset.PnOffset"
    """<p>Pseudo-noise offset, which is a characteristic of the signal from a cell on a radio tower.</p>"""
    cdma_channel: "aws_sdk_iot_wireless.types.cdma_channel.CdmaChannel"
    """<p>CDMA channel information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CdmaLocalId) -> dict:
    out: dict = {}
    out["PnOffset"] = value["pn_offset"]
    out["CdmaChannel"] = value["cdma_channel"]
    return out


def deserialize_json(data: dict) -> CdmaLocalId:
    out: CdmaLocalId = {}  # type: ignore[typeddict-item]
    if "PnOffset" in data:
        out["pn_offset"] = data["PnOffset"]
    else:
        raise DeserializationError("CdmaLocalId.pn_offset required")
    if "CdmaChannel" in data:
        out["cdma_channel"] = data["CdmaChannel"]
    else:
        raise DeserializationError("CdmaLocalId.cdma_channel required")
    return out
