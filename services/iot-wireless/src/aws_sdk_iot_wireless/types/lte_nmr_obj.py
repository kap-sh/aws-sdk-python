"""Generated from Smithy shape ``com.amazonaws.iotwireless#LteNmrObj``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.earfcn
    import aws_sdk_iot_wireless.types.eutran_cid
    import aws_sdk_iot_wireless.types.pci
    import aws_sdk_iot_wireless.types.rsrp
    import aws_sdk_iot_wireless.types.rsrq


class LteNmrObj(TypedDict):
    pci: "aws_sdk_iot_wireless.types.pci.PCI"
    """<p>Physical cell ID.</p>"""
    earfcn: "aws_sdk_iot_wireless.types.earfcn.EARFCN"
    """<p>E-UTRA (Evolved universal terrestrial Radio Access) absolute radio frequency channel Number (EARFCN).</p>"""
    eutran_cid: "aws_sdk_iot_wireless.types.eutran_cid.EutranCid"
    """<p>E-UTRAN (Evolved Universal Terrestrial Radio Access Network) cell global identifier (EUTRANCID).</p>"""
    rsrp: NotRequired["aws_sdk_iot_wireless.types.rsrp.RSRP"]
    """<p>Signal power of the reference signal received, measured in dBm (decibel-milliwatts).</p>"""
    rsrq: NotRequired["aws_sdk_iot_wireless.types.rsrq.RSRQ"]
    """<p>Signal quality of the reference Signal received, measured in decibels (dB).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteNmrObj) -> dict:
    out: dict = {}
    out["Pci"] = value["pci"]
    out["Earfcn"] = value["earfcn"]
    out["EutranCid"] = value.get("eutran_cid", 0)
    if "rsrp" in value:
        out["Rsrp"] = value["rsrp"]
    if "rsrq" in value:
        out["Rsrq"] = value["rsrq"]
    return out


def deserialize_json(data: dict) -> LteNmrObj:
    out: LteNmrObj = {}  # type: ignore[typeddict-item]
    if "Pci" in data:
        out["pci"] = data["Pci"]
    else:
        raise DeserializationError("LteNmrObj.pci required")
    if "Earfcn" in data:
        out["earfcn"] = data["Earfcn"]
    else:
        raise DeserializationError("LteNmrObj.earfcn required")
    if "EutranCid" in data:
        out["eutran_cid"] = data["EutranCid"]
    else:
        out["eutran_cid"] = 0
    if "Rsrp" in data:
        out["rsrp"] = data["Rsrp"]
    if "Rsrq" in data:
        out["rsrq"] = data["Rsrq"]
    return out
