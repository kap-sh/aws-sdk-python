"""Generated from Smithy shape ``com.amazonaws.iotwireless#LteObj``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.eutran_cid
    import aws_sdk_iot_wireless.types.lte_local_id
    import aws_sdk_iot_wireless.types.lte_nmr_list
    import aws_sdk_iot_wireless.types.lte_timing_advance
    import aws_sdk_iot_wireless.types.mcc
    import aws_sdk_iot_wireless.types.mnc
    import aws_sdk_iot_wireless.types.nr_capable
    import aws_sdk_iot_wireless.types.rsrp
    import aws_sdk_iot_wireless.types.rsrq
    import aws_sdk_iot_wireless.types.tac


class LteObj(TypedDict):
    mcc: "aws_sdk_iot_wireless.types.mcc.MCC"
    """<p>Mobile Country Code.</p>"""
    mnc: "aws_sdk_iot_wireless.types.mnc.MNC"
    """<p>Mobile Network Code.</p>"""
    eutran_cid: "aws_sdk_iot_wireless.types.eutran_cid.EutranCid"
    """<p>E-UTRAN (Evolved Universal Terrestrial Radio Access Network) Cell Global Identifier.</p>"""
    tac: NotRequired["aws_sdk_iot_wireless.types.tac.TAC"]
    """<p>LTE tracking area code.</p>"""
    lte_local_id: NotRequired["aws_sdk_iot_wireless.types.lte_local_id.LteLocalId"]
    """<p>LTE local identification (local ID) information.</p>"""
    lte_timing_advance: NotRequired[
        "aws_sdk_iot_wireless.types.lte_timing_advance.LteTimingAdvance"
    ]
    """<p>LTE timing advance.</p>"""
    rsrp: NotRequired["aws_sdk_iot_wireless.types.rsrp.RSRP"]
    """<p>Signal power of the reference signal received, measured in dBm (decibel-milliwatts).</p>"""
    rsrq: NotRequired["aws_sdk_iot_wireless.types.rsrq.RSRQ"]
    """<p>Signal quality of the reference Signal received, measured in decibels (dB).</p>"""
    nr_capable: "aws_sdk_iot_wireless.types.nr_capable.NRCapable"
    """<p>Parameter that determines whether the LTE object is capable of supporting NR (new radio).</p>"""
    lte_nmr: NotRequired["aws_sdk_iot_wireless.types.lte_nmr_list.LteNmrList"]
    """<p>LTE object for network measurement reports.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LteObj) -> dict:
    out: dict = {}
    out["Mcc"] = value["mcc"]
    out["Mnc"] = value["mnc"]
    out["EutranCid"] = value["eutran_cid"]
    if "tac" in value:
        out["Tac"] = value["tac"]
    if "lte_local_id" in value:
        import aws_sdk_iot_wireless.types.lte_local_id

        out["LteLocalId"] = aws_sdk_iot_wireless.types.lte_local_id.serialize_json(
            value["lte_local_id"]
        )
    if "lte_timing_advance" in value:
        out["LteTimingAdvance"] = value["lte_timing_advance"]
    if "rsrp" in value:
        out["Rsrp"] = value["rsrp"]
    if "rsrq" in value:
        out["Rsrq"] = value["rsrq"]
    out["NrCapable"] = value.get("nr_capable", False)
    if "lte_nmr" in value:
        import aws_sdk_iot_wireless.types.lte_nmr_list

        out["LteNmr"] = aws_sdk_iot_wireless.types.lte_nmr_list.serialize_json(
            value["lte_nmr"]
        )
    return out


def deserialize_json(data: dict) -> LteObj:
    out: LteObj = {}  # type: ignore[typeddict-item]
    if "Mcc" in data:
        out["mcc"] = data["Mcc"]
    else:
        raise DeserializationError("LteObj.mcc required")
    if "Mnc" in data:
        out["mnc"] = data["Mnc"]
    else:
        raise DeserializationError("LteObj.mnc required")
    if "EutranCid" in data:
        out["eutran_cid"] = data["EutranCid"]
    else:
        raise DeserializationError("LteObj.eutran_cid required")
    if "Tac" in data:
        out["tac"] = data["Tac"]
    if "LteLocalId" in data:
        import aws_sdk_iot_wireless.types.lte_local_id

        out["lte_local_id"] = aws_sdk_iot_wireless.types.lte_local_id.deserialize_json(
            data["LteLocalId"]
        )
    if "LteTimingAdvance" in data:
        out["lte_timing_advance"] = data["LteTimingAdvance"]
    if "Rsrp" in data:
        out["rsrp"] = data["Rsrp"]
    if "Rsrq" in data:
        out["rsrq"] = data["Rsrq"]
    if "NrCapable" in data:
        out["nr_capable"] = data["NrCapable"]
    else:
        out["nr_capable"] = False
    if "LteNmr" in data:
        import aws_sdk_iot_wireless.types.lte_nmr_list

        out["lte_nmr"] = aws_sdk_iot_wireless.types.lte_nmr_list.deserialize_json(
            data["LteNmr"]
        )
    return out
